from genderbias.detector import Detector, Flag, Issue, Report
import os

"""
Letters for women are more likely to include grindstone adjectives than standout
words.

"Standout words, which portray a candidate as talented and exciting, are most often
found in letters of recommendation for men. Grindstone words, which create the impression
that a candidate works hard but is not intellectually exceptional, are more often
used for women." (Blue et al. 2018)

Citations:
Assessing Gender Bias in Particle Physics and Social Science Recommendations for Academic Jobs
Exploring the color of glass: letters of recommendation for female and male medical faculty

Goal: Check for grindstone words.
"""
_dir = os.path.dirname(__file__)
print(_dir)
GRINDSTONE_WORDS = [word.strip() for word in open(_dir + "/grindstone.wordlist", 'r').readlines()]
STANDOUT_WORDS = [w.strip() for w in open(_dir + "/standout.wordlist", 'r').readlines()]

class GrindstoneDetector(Detector):

    def get_report(self, doc):
        grindstone_report = Report("grindstone")
        words_with_indices = doc.words_with_indices()

        found_standout = False
        found_grindstone = False
        for word, start, stop in words_with_indices:

            if word.lower() in STANDOUT_WORDS:
                found_standout = True
                grindstone_report.add_flag(
                    Flag(start, stop, Issue("standoutWord",
                                            " '{word}' is an standout word.".format(
                                                word=word), bias=Issue.positive_result)))
            if word.lower() in GRINDSTONE_WORDS:
                found_grindstone = True
                grindstone_report.add_flag(
                    Flag(start, stop, Issue(
                        "grindstoneWord",
                        " '{word}' is a grindstone word.".format(
                            word=word),
                        "Grindstone words should be replaced with standout words."
                    ))
                )

        if found_grindstone and found_standout:
            grindstone_report.set_summary("Found some grindstone words used to describe the subject as well as standout words. Consider the necessity of the grindstone words and if they can be changed to standout adjectives.")
        elif found_grindstone:
            grindstone_report.set_summary("There were some grindstone words, but no standout words. Grindstone words make it appear as though the subject does not possess an inate ability. Consider replacing grindstone words such as 'hardworking' or 'tenacious' with standout words such as 'outstanding' or 'amazing' as it shows inherent skill.")
        elif found_standout:
            grindstone_report.set_summary("There were no grindstone words, but did contain standout words. This is okay.")

        return grindstone_report
