# Understanding Detectors

Various detectors have been implemented with the intent to test for bias in letters of recommendation.

## Description
This project investigates various detectors as a way to determine bias in letters of recommendation. Each detector has been thoughtfully chosen and developed. The reasoning behind the detectors is included along with citations for those curious.

NOTE: I will need to change these links when merging because they link to forked repo.

###### AVAILABLE DETECTORS:
* [FemaleDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/femalewords)
  * A detector for words that tend to be used more frequently for recruiting women than for recruiting men.
* [MaleDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/malewords)
  * Detect words that are more commonly used to recruit men rather than women.
* [GenderedWordDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/genderedwords)
  * This detector checks for words that call unnecessary attention to the gender of the letter recipient.
* [PersonalLifeDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/personal_life)
  * Letters for women are more likely to discuss personal life.
* [PublicationDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/publications)
  * Letters for women are less likely to mention publications and projects
* [EffortDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/effort)
  * Letters for women are more likely to highlight effort (she is hard-working) instead of highlighting accomplishments (her research is groundbreaking).
* [GrindstoneDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/grindstone)
  * This will be combined with the effort detector. Should I combine these to? There are different word lists and grindstone ones seems to be a subset of effort detector, I am unsure as the source for the effort detector wordlist. Grindstone detector is directly from a paper: [Gender Matters](https://physicstoday.scitation.org/doi/10.1063/PT.3.3870).
* [AgenticDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/agentic)
  * Letters for women are less likely to include agentic words and more likely to include communal terms (Madera).
* [ConditionalSuperlativesDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/conditionalsuperlatives)
  * This detector checks for conditional superlatives, or superlatives that are "hedged" by restricting the population to only women. These are phrases like "the best woman for the job" or "best of all women" that are clear 'hedged' superlatives
* [SuperlativeDetector](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/superlatives)
  * Letters for women are less likely to contain superlatives (best, most, top, greatest). If they contain superlatives, they usually describe women in the context of emotional terms (she was the most compassionate).
* [Repetition](https://github.com/ajrichter7/gender-bias/tree/master/genderbias/repetition)
  * Letters for men are far more likely to repeat positive words than letters for women: Here we found that the letters for women that had at least one of these terms had an average of 1.5 terms, whereas the letters for men that included at least one had an average of 2.0 such terms. That is, there was repetition of standout adjectives within men’s letters to a greater extent. (Trix & Psenka 2003, pg 18(208))

###### WORK TO BE DONE:
  * Gender stereotypes for emotion-focused words
    * **This one already exists in the form of female and male detector. I also believe it is the same as agentic detector.** I am unsure if I should just remove the agentic one and then like mark this as completed as it uses regex and seems to be working in two different detectors (female/male).
    * Letters for women are more likely to include gender stereotypes (she is compassionate vs he is a leader) and emotion-focused words.
      * **Goal:** Develop code that can read text for words and gender stereotypes and highlight them (Word List). Return a summary statement that directs the author to review the highlighted words and evaluate whether they are relevant for the recommendation or evaluation. If the emotion-focused words are relevant to the letter or evaluation, suggest that the author include additional statements that balance them out and highlight other relevant areas like skills and accomplishments.
      * *Note on the word list:* some of the words are incomplete, for example "shar" is included so that it  captures sharing or shared or share.

###### INCOMPLETE DETECTORS:
**I need help figuring out how to do these last two!**
* Minimal Assurance
  * Letters for women are more likely to include minimal assurance (she can do the job) rather than a strong endorsement (he has all the necessary skills to excel in this position).
    * **Goal:** Develop code that can read text for minimal assurance. If the text includes minimum assurance statements, return a summary statement that directs the author to remove the minimal assurance and replace it a strong endorsement. If the text lacks strong endorsements, return a summary statement that directs the author to add one.
* Adjective Usage
  * Letters for women are more likely to use adjectives instead of nouns
    * **Goal:** Develop code that can read text for the presence of nouns that highlight roles/positions (like leader, researcher). If position nouns are absent, return a summary statement that directs the author to consider using nouns to strengthen the letter.
    * This one can be complicated. The goal is to differentiate between descriptions that use adjectives, verbs, or weaken the position noun (i.e., she was involved in research, she taught).


## Getting Started

A note on using macOS. There can be some difficulty in getting

```
genderbias -h
```
to work in the terminal if using a newer version on macOS. Make sure to configure the PATH to contain
genderbias and where you stored the requirements. In order to do this, newer versions use zsh instead of bash so you want to update *.zshrc* instead of *.bashrc* or *.bash_profile*.

To determine what shell you are using, run the command
```
echo $SHELL
```

### How to Run Detectors

Detectors can be run individually by specifying what detector you want to run.

A list of detectors can be displayed through the command

```
genderbias --list-detectors
```
1. You can run them on files by
```
genderbias -f ./example_letters/letterofRecW --detectors  Detector    
```
where you can specify the path to a file and multiple or one detector to run, be sure to change Detector to a specific detector.

2. You can run them on text in the terminal through using
```
echo "insert text here" | genderbias --detector Detector
```
and insert the text you want to test and be sure to change Detector to a specific detector.


### How to Write Detectors

There is a lovely guide for writing new detectors linked [here](https://github.com/gender-bias/gender-bias/tree/master/docs/hacking). It was created by [Jordan Matelsky](https://github.com/j6k4m8) for those who are interested in either writing new detectors or understanding the code for the existing detectors.

## Help

Open a new issue for any questions and it will be addressed as quickly as possible. Also, feel free to contact the creators for clarification or if something is no longer working.


## Authors
Project started by Mollie Marr with Jordan Matelsky being a main contributor.

This read me was authored by [Alex Richter](https://github.com/ajrichter7) (she/her).
