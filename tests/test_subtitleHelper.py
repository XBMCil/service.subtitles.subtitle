# -*- coding: utf-8 -*-
import test_helpers
from unittest import TestCase
from resources.lib.SUBUtilities import SubtitleHelper, parse_rls_title


class TestSubtitleHelper(TestCase):
    def setUp(self):
        self.helper = SubtitleHelper()

    def test_get_subtitle_list(self):
        item = {'episode': '1', 'title': 'The Blood of Man', 'season': '2', 'year': '', 'tvshow': "Da Vinci's Demons",
                '3let_language': ['eng', 'heb']}

        result = self.helper._search_tvshow(item)
        self.assertEqual(result[0]['name'], 'da vinci s demons')

    def test_get_subtitle_list2(self):
        item = {'episode': '', 'title': 'Two.and.a.Half.Men.S11E13.480p.HDTV.X264-DIMENSION',
                'season': '', 'year': '', 'tvshow': '', '3let_language': ['en', 'he']}

        parse_rls_title(item)
        result = self.helper._search_tvshow(item)
        self.assertEqual(result[0]['name'], 'two and a half men')

    def test_get_subtitle_list3(self):
        item = {'episode': '', 'title': 'Broken Arrow', 'season': '', 'year': '1997',
                'tvshow': '', '3let_language': ['en', 'he']}

        result = self.helper._search_movie(item)
        self.assertEqual(result[0]['name'], 'broken arrow')
        self.assertEqual(result[0]['year'], '1996')

    def test_get_subtitle_list4(self):
        item = {'episode': '', 'title': 'The.Flash.2014.S02E05.480p.HDTV.X264-DIMENSION.mkv',
                'preferredlanguage': 'heb', 'season': '', 'year': '', 'tvshow': '', '3let_language': ['heb']}

        parse_rls_title(item)
        result = self.helper._search_tvshow(item)
        self.assertEqual(result[0]['name'], 'the flash')

    def test_get_subtitle_list5(self):
        item = {'episode': '18', 'title': 'The Singularity', 'preferredlanguage': 'heb', 'season': '3',
                'year': '2013', 'tvshow': "Agents of S.H.I.E.L.D.",
                '3let_language': ['heb']}

        parse_rls_title(item)
        result = self.helper._search_tvshow(item)

        self.assertEqual(result[0]['name'], 'agents of s h i e l d ')
