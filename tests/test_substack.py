from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from sync_substack import parse_feed, merge_candidates, plain
class SubstackTests(unittest.TestCase):
    origins=['https://fixture.substack.com']
    def feed(self):
        return b'''<rss><channel><item><title>Essay A</title><link>https://fixture.substack.com/p/a?utm_source=x</link><pubDate>Fri, 23 Oct 2026 08:00:00 GMT</pubDate><description>&lt;p&gt;An essay&lt;/p&gt;&lt;script&gt;alert(1)&lt;/script&gt;</description></item><item><title>Essay B</title><link>https://fixture.substack.com/p/b</link><pubDate>Thu, 22 Oct 2026 08:00:00 GMT</pubDate><description>Second essay</description></item></channel></rss>'''
    def test_sanitize(self): self.assertEqual(plain('<p>Hello</p><script>x</script>world'),'Hello world')
    def test_two_metadata_cards(self):
        rows=parse_feed(self.feed(),self.origins)
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['description'],'An essay')
        self.assertNotIn('?',rows[0]['canonical_url'])
        self.assertEqual(rows[0]['visibility'],'draft')
    def test_retains_history_and_owner_flags(self):
        rows=parse_feed(self.feed(),self.origins); rows[0]['hidden']=True; rows[0]['topics']=['reviewed']
        result=merge_candidates(rows,parse_feed(self.feed(),self.origins)[:1],[])
        self.assertEqual(len(result),2)
        self.assertTrue(result[0]['hidden'])
        self.assertEqual(result[0]['topics'],['reviewed'])
    def test_curated_wins(self):
        rows=parse_feed(self.feed(),self.origins)
        self.assertEqual(merge_candidates([],rows,rows),[])
    def test_empty_feed_keeps_history(self):
        rows=parse_feed(self.feed(),self.origins)
        self.assertEqual(len(merge_candidates(rows,parse_feed(b'<rss><channel/></rss>',self.origins),[])),2)
    def test_wrong_origin(self):
        with self.assertRaises(ValueError): parse_feed(self.feed(),['https://other.substack.com'])
    def test_malformed_feed(self):
        with self.assertRaises(Exception): parse_feed(b'<rss>',self.origins)
    def test_entities_rejected(self):
        with self.assertRaises(ValueError): parse_feed(b'<!DOCTYPE rss><rss><channel/></rss>',self.origins)
