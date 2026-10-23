from pathlib import Path
import sys
import tempfile
import unittest
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from render_content import generate
from content import native_posts, validate
from sync_substack import parse_feed
class WritingRenderingTests(unittest.TestCase):
    def test_native_and_two_external_cards(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'content').mkdir(); post=root/'writing/posts/native/index.qmd'; post.parent.mkdir(parents=True)
            post.write_text('---\nid: local:native\ntitle: Fixture native note\ndate: 2026-10-23\ndescription: An original note\nvisibility: public\ntopics: [topic]\n---\nOriginal fixture text.\n')
            essays=[dict(id='essay-'+x,title='Fixture essay '+x,date='2026-10-22',canonical_url='https://fixture.substack.com/p/'+x,source='substack',description='Metadata only',topics=['topic'],visibility='public') for x in ['a','b']]
            data={'research':[dict(id='topic',name='Topic',question='Question?',visibility='public')],'publications':[],'projects':[],'substack':essays,'news':[]}
            for name,rows in data.items(): (root/'content'/f'{name}.yml').write_text(yaml.safe_dump(rows))
            generate(root)
            html=(root/'_generated/writing.html').read_text()
            self.assertIn('Fixture native note',html)
            self.assertIn('On this site',html)
            self.assertEqual(html.count('<span class="badge-label">Substack</span>'),2)
            self.assertNotIn('Original fixture text',html)
            self.assertIn('https://fixture.substack.com/p/a',html)
            self.assertEqual(validate(data,native_posts(root)),[])
            # A draft in the direct-render tree must fail, not just disappear from its index.
            post.write_text(post.read_text().replace('visibility: public','visibility: draft'))
            with self.assertRaises(ValueError): generate(root)
