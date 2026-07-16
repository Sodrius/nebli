import unittest
from prefiltrar_pool import particionar


class PrefilterTests(unittest.TestCase):
    def test_step2_only_is_noise(self):
        card = {"front": "Normal anatomy", "tags": ["#AK_Step2_v12::Cardiology"]}
        good, noise = particionar([card], ["carcinoma"])
        self.assertFalse(good)
        self.assertEqual(noise[0][1], "Step2-only")

    def test_step1_and_step2_overlap_is_kept(self):
        card = {"front": "Normal anatomy", "tags": ["#AK_Step1_v12::X", "#AK_Step2_v12::X"]}
        good, noise = particionar([card], ["carcinoma"])
        self.assertEqual(good, [card])
        self.assertFalse(noise)


if __name__ == "__main__":
    unittest.main()
