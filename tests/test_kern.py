"""
This file contains test functions for KERN import and export.
"""
import unittest

import partitura
from tests import KERN_TESFILES
from partitura.score import merge_parts
from partitura.utils import ensure_notearray
from partitura.io.importkern import load_kern
from partitura import load_musicxml
import numpy as np

class TestImportKERN(unittest.TestCase):

    def test_example_kern(self):
        document_path = partitura.EXAMPLE_KERN
        kern_part = merge_parts(load_kern(document_path))
        xml_part = load_musicxml(partitura.EXAMPLE_MUSICXML)
        ka = ensure_notearray(kern_part)
        xa = ensure_notearray(xml_part)
        self.assertTrue(np.all(ka["onset_beat"] == xa["onset_beat"]) , "Kern onset beats do not match target")
        self.assertTrue(np.all(ka["duration_beat"] == xa["duration_beat"]),
                        "Kern duration beats do not match target.")

    def test_examples(self):
        for fn in KERN_TESFILES:
            parts = merge_parts(load_kern(fn))
