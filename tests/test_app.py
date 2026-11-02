# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location("app",Path(__file__).resolve().parents[1]/"coderain.py")
app=importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class Tests(unittest.TestCase):
    def test_frame(self):
        text=app.frame("Hamdy",60,color=False)
        self.assertEqual(len(text),60)
        self.assertIn("Hamdy",text)

    def test_narrow_terminal(self):
        self.assertEqual(len(app.frame("Very long name",4,False)),4)
        with self.assertRaises(ValueError):app.frame("X",0,False)

if __name__=="__main__":unittest.main()
