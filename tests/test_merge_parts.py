#!/usr/bin/env python
import numpy as np
import logging
import unittest
from pathlib import Path

from partitura import load_musicxml
from partitura.score import merge_parts
from partitura.utils.music import note_array_from_part

from tests import MERGE_PARTS_TESTFILES

LOGGER = logging.getLogger(__name__)


class TestMergeParts(unittest.TestCase):
    """
    Test merge parts utility
    """

    def test_list_of_parts_and_partgroup(self):
        parts = load_musicxml(MERGE_PARTS_TESTFILES[1])
        merged_part = merge_parts(parts)
        note_array = merged_part.note_array
        expected_onsets = [0, 0, 0, 0, 0, 0, 12, 15, 24, 24, 32, 40, 48]
        expected_pitches = [69, 67, 53, 48, 62, 50, 64, 65, 69, 47, 67, 64, 60]
        self.assertTrue(np.array_equal(note_array["onset_div"], expected_onsets))
        self.assertTrue(np.array_equal(note_array["pitch"], expected_pitches))

    def test_different_divs(self):
        parts = load_musicxml(MERGE_PARTS_TESTFILES[2])
        merged_part = merge_parts(parts)
        note_array = merged_part.note_array
        expected_onsets = [0, 0, 0, 0, 0, 0, 12, 15, 24, 24, 32, 40, 48]
        expected_pitches = [69, 67, 53, 48, 62, 50, 64, 65, 69, 47, 67, 64, 60]
        self.assertTrue(np.array_equal(note_array["onset_div"], expected_onsets))
        self.assertTrue(np.array_equal(note_array["pitch"], expected_pitches))

    def test_merge_single_part(self):
        parts = load_musicxml(MERGE_PARTS_TESTFILES[3])
        merged_part = merge_parts(parts)
        self.assertTrue(merged_part == parts)

