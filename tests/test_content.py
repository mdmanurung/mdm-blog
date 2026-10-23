import copy
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from content import canonical, norm_doi, validate, ROOT, load
from render_content import generate, publication
import yaml

class ContentTests(unittest.TestCase):
    def setUp(self):
        self.data = {'research':[{'id':'topic','name':'Topic','question':'Question?','visibility':'public'}], 'projects':[], 'substack':[], 'news':[], 'publications':[]}
        self.paper = dict(id='doi:10.1234/test', doi='10.1234/test',title='Fixture research',year=2026,venue='Fixture',authors=['A. Author'],status='preprint',topics=['topic'],paper_url='https://doi.org/10.1234/test',visibility='draft')
    def test_repository_data_valid(self): self.assertEqual(validate(load()),[])
    def test_duplicate_doi(self):
        self.data['publications']=[self.paper,dict(self.paper,id='other')]
        self.assertIn('duplicate DOI',' '.join(validate(self.data)))
    def test_unknown_topic(self):
        self.data['publications']=[dict(self.paper,topics=['absent'])]
        self.assertIn('unknown topics',' '.join(validate(self.data)))
    def test_no_public_synthetic(self):
        self.data['publications']=[dict(self.paper,visibility='public',synthetic=True)]
        self.assertIn('synthetic records',' '.join(validate(self.data)))
    def test_public_requires_approval(self):
        self.data['publications']=[dict(self.paper,visibility='public')]
        self.assertIn('approval provenance',' '.join(validate(self.data)))
    def test_url_security(self):
        self.data['substack']=[dict(id='essay',title='Essay',canonical_url='javascript:alert(1)',date='2026-10-23',visibility='draft',topics=['topic'])]
        self.assertIn('invalid canonical',' '.join(validate(self.data)))
    def test_normalization(self):
        self.assertEqual(norm_doi('https://doi.org/10.1234/ABC'),'10.1234/abc')
        self.assertEqual(canonical('https://writer.substack.com/p/a/?utm_source=x#top'),'https://writer.substack.com/p/a')
    def test_public_draft_relation_rejected(self):
        self.data['publications']=[self.paper]
        self.data['projects']=[dict(id='tool',title='Tool',repository='owner/tool',maturity='experimental',summary='Summary',audience='researchers',topics=['topic'],visibility='public',paper_ids=[self.paper['id']])]
        self.assertIn('references draft paper',' '.join(validate(self.data)))
    def test_draft_does_not_render(self):
        self.data['publications']=[dict(self.paper,title='SECRET DRAFT TITLE')]
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'content').mkdir()
            for kind,rows in self.data.items(): (root/'content'/f'{kind}.yml').write_text(yaml.safe_dump(rows))
            generate(root)
            self.assertNotIn('SECRET DRAFT TITLE',''.join(x.read_text() for x in (root/'_generated').glob('*')))
    def test_untrusted_text_escaped(self):
        p=dict(self.paper,title='<img onerror=alert(1)>',authors=['<script>'])
        text=publication(p,{'topic':self.data['research'][0]})
        self.assertNotIn('<img',text)
        self.assertIn('&lt;script&gt;',text)

if __name__=='__main__': unittest.main()
