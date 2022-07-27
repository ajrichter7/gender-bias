from genderbias.detector import Detector, Flag, Issue, Report
import os

"""
Letters for women are less likely to contain superlatives (best, most, top, greatest).
If they contain superlatives, they usually describe women in the context of emotional terms (she was the most compassionate).

Goal: Develop code that can read text for superlatives. If the text lacks superlatives,
return a summary statement that directs the author to add superlatives.

If superlatives are present, search for the adjectives or nouns associated with the superlative.
If they are emotion or gendered terms (compassion), return a summary statement that directs
the author to add superlatives that include accomplishments, skills, or capabilities.
"""
_dir = os.path.dirname(__file__)
SUPERLATIVE_WORDS = [word.strip() for word in open(_dir + "/superlative.wordlist", 'r').readlines()]
GENDERED_WORDS = [w.strip() for w in open(_dir + "/genderedwords.wordlist", "r").readlines()]

class SuperlativeDetector(Detector):

    def get_report(self, doc):
        superlative_report = Report("superlatives")
        words_with_indices = doc.words_with_indices()
        found_negative_superlative = False
        found_positive_superlative = False

        for i in range(len(words_with_indices)):
            word = words_with_indices[i][0]
            start = words_with_indices[i][1]
            stop = words_with_indices[i][2]

            if word.lower() in SUPERLATIVE_WORDS and words_with_indices[i+1][0] in GENDERED_WORDS:
                found_negative_superlative = True
                superlative_report.add_flag(
                    Flag(start, stop, Issue(
                        "superlativeWord",
                        "Be careful in using superlatives because in most cases they apply to emotional terms for women. '{word}' is an superlative-sounding word.".format(
                            word=word),
                        "Try replacing with phrasing that emphasizes that this person's skills that are job related and not emotion based."
                    ))
                )

            elif word.lower() in SUPERLATIVE_WORDS:
                found_positive_superlative = True
                superlative_report.add_flag(
                Flag(start, stop, Issue("superlativeWord",
                        "This word seems fine in this context.",
                        bias=Issue.positive_result)))

        if found_positive_superlative or found_negative_superlative:
            superlative_report.set_summary("Found some superlative words. Make sure to double check the context of these words. If describing something strictly related to the position, such as 'NAME is the top of their class' that is is okay. If it is emotional, such as 'NAME is the most compassionate employee', change this phrase.")
        else:
            superlative_report.set_summary("There were no superlative words. Consider adding some that relate to accomplishment instead of character, such as 'NAME is the most accomplished undergraduate' as opposed to 'NAME is the most compassionate'. Describe accomplishments over emotion or character.")

        return superlative_report
