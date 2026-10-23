import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from sync_publications import discover
class DiscoveryTests(unittest.TestCase):
    def test_identity_missing(self):
        self.assertIsNone(discover({},lambda _:self.fail('must not fetch')))
    def test_pagination_deduplication(self):
        responses=iter([{'results':[{'id':'https://openalex.org/W1','doi':'https://doi.org/10.1234/A','display_name':'A'}],'meta':{'next_cursor':'next'}},{'results':[{'id':'https://openalex.org/W1','doi':'https://doi.org/10.1234/A','display_name':'A'}],'meta':{'next_cursor':None}}])
        rows=discover({'openalex_author_ids':['A1']},lambda _:next(responses))
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['doi'],'10.1234/a')
        self.assertEqual(rows[0]['visibility'],'draft')
    def test_provider_error_propagates(self):
        def fail(_): raise OSError('offline')
        with self.assertRaises(OSError): discover({'openalex_author_ids':['A1']},fail)
