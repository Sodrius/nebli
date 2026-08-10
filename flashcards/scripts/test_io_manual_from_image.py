#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from io_manual_from_image import draw_answer_preview, draw_question_preview


class ImageOcclusionPreviewTests(unittest.TestCase):
    def test_question_masks_label_box_and_answer_reveals_it(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            image = Image.new("RGB", (100, 60), "white")
            labels = [{"text": "Thoracic part", "box": [20, 20, 40, 10]}]
            question = root / "question.png"
            answer = root / "answer.png"
            draw_question_preview(image, labels, question)
            draw_answer_preview(image, labels, answer)

            self.assertEqual(Image.open(question).getpixel((40, 25)), (92, 101, 112))
            self.assertEqual(Image.open(answer).getpixel((40, 25)), (255, 255, 255))


if __name__ == "__main__":
    unittest.main()
