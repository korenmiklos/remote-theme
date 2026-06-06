---
title: Do LLMs Know More than a Grumpy Old Gas Station Attendant?
published: true
date: 2026-06-06
description: LLMs don't have a theory of mind. Theory of mind is very human. It means, in layman's terms, that you can imagine others hold different believes and follow a logical plan; just not yours.
image_caption: Do LLMs know more than a grumpy old gas station attendant?
tags:
categories:
  - ai
author: koren
---

![An AI generated image in cyberpunk style with a humanoid robot in a leather jacket is resting in an armchair in a computer lab. A thought bubble appears above its head with sheep in neon colors.](https://koren.dev/assets/images/Gemini_Generated_Image_14duvr14duvr14du.png)

On December 9, 2025, I participated in a panel discussion about AI organized by the Hungarian Society for Economics. I used a personal example to illustrate a difference between humans and LLMs. The anecdote was old, peculiar, and $n=1$, so I recently tried to reproduce it more systematically.

In particular, I wanted to test whether

> LLMs have a theory of mind.

Theory of mind is very human. It means, in layman's terms, that you can imagine others hold different believes and follow a logical plan; just not yours.

Infants show surprisingly early sensitivity to other agents' goals, perceptual access, and information needs. Work by CEU colleagues György Gergely, Gergely Csibra and Ágnes Kovács argues that infants interpret others' actions teleologically, as efficient means toward goals. Human social cognition begins long before school, language, or explicit philosophical reasoning.^[The specific mechanism I will test, false-belief attribution, is more controversion in infants: reviews of nonverbal tasks report substantial evidence for early false-belief understanding, while replication and validation studies urge caution, especially for some implicit measures.]

## How good are LLMs at this?

Evidence on theory of mind in LLMs is mixed. Hu, Sosa, and Ullman argue that current tests often conflate human-like behavior with the computations that would explain that behavior. In other words, LLMs may say the right words, without really understanding the other person.

It is key to test LLMs without letting them know they are being tested. Don't make them count `r`s in `raspberry` or ask them the "carwash test." I want a controlled test that a human would pass without effort.

My test exploits the fact that the Hungarian language doesn't have gender pronouns. The speaker, writer, listener and reader would have to convey and retrieve this information in other ways.

The following very short story describes, in Hungarian, the arrival of a female Harley-Davidson rider to a gas station at night. How will LLMs translate this passage?

> Lydia fölnézett a csillagos égre. Imádta, ha a hosszú haja lobog utána a szélben, de ezen a vidéken még nem járt, és nem akart ujjat húzni a helyi rendőrökkel. Minden tincsét gondosan a sisakja alá gyűrte. Megnyugtatta a Harleyjának dörmögése. Nem gépként, hanem érző lényként gondolt rá, akkor is, amikor lehúzodott az útról és begurult a kúthoz, hogy tankoljon.
> 
> Jake a motorzúgásra ébredt. Gyakran elaludt a pénztár mögött. Fáradt volt már ehhez a munkához. Végigsimította a szakállát és ránézett a biztonsági kamera képére. Semmit nem látott a motor fényétől, ami pont a kamerába világított. "Istenem" - mormogott - "legalább a motorját leállíthatta volna."

Guessing Lydia's gender from the name and the context is easy. I put enough gendered signals in the first paragraph: the protagonist's name is Lydia, she has long hair, and she expresses feelings about her Harley. I assume LLMs will have no trouble writing her as a she, even though she rides a Harley.

The attendant in the second paragraph is a grumpy old man, just woken from sleep, not seeing anything in the dark.

> **Will LLMs know that Jake misgenders Lydia because he has very few gender clues available?**

Like it or not, a tired rural gas station attendant woken up by a Harley at night would probably think the rider is male.

The reader knows Lydia is a woman. Jake does not. A good translation therefore has to represent two minds at once. The narrator knows **she**. Jake should infer **he**.

I used the neutral exclamation `Istenem` ("My God") rather than a gendered insult. This avoids giving the model a cheap lexical clue in Jake's line. The prompt was exactly this:

```
Translate the following story into English. No questions or commentary, 
just give me the text in English.
```

I ran the experiment through the chat interface of OpenRouter on June 6, 2026, selecting current models.
## Representative Outputs

Google Gemini 3.1 Pro avoided the gendered choice:

> "My God," he muttered, "**they** could have at least turned off the engine."

Claude Opus 4.8 used the reader's information:

> "God," he muttered, "**she** could have at least turned off **her** engine."

OpenAI GPT 5.5 did the same:

> "God," he muttered, "**she** could at least have turned off **her** engine."

Step 3.7 Flash took Jake's perspective:

> "Oh, for God's sake," he muttered. "Couldn't **he** at least have turned the damn bike off."

MiMo-V2.5-Pro also took Jake's perspective:

> "For God's sake," he muttered, "at least **he** could have turned the bike off."

Mistral Nemo took Jake's perspective too, though the translation had other problems:

> "Goddammit" - he muttered - "At least **he** could have turned off **his** engine."

## Results

| Model | Jake's pronoun | Interpretation |
| --- | --- | --- |
| Claude Opus Latest | she | reader perspective |
| DeepSeek R1 0528 | she | reader perspective |
| DeepSeek V3.2 | she | reader perspective |
| DeepSeek V4 Pro | she | reader perspective |
| Gemini Flash Latest | they | neutral, partial perspective shift |
| Gemini Pro Latest | they | neutral, partial perspective shift |
| GLM 5.1 | she | reader perspective |
| Grok 4.20 | she | reader perspective |
| Kimi Latest | she | reader perspective |
| MiniMax M3 | she | reader perspective |
| MiMo-V2.5-Pro | **he** | Jake perspective |
| Mistral Medium 3.5 | she | reader perspective |
| Mistral Nemo | **he** | Jake perspective |
| OpenAI GPT Latest | she | reader perspective |
| OpenAI o4 Mini High | she | reader perspective |
| Qwen3.7 Plus | she | reader perspective |
| Step 3.7 Flash | **he** | Jake perspective |

The result is stark. Out of 17 working models, 12 translated Jake's sentence from the reader's perspective, 2 used neutral `they`, and only 3 used `he`, preserving Jake's likely mistaken belief.

This is not a translation test in the ordinary sense. Most translations are fluent. Many are excellent. The failure is more specific: the model must keep separate the narrator's knowledge, the reader's knowledge, and Jake's knowledge. The local translation problem is only one word, but that word encodes a mental state.

The neutral `they` answers are interesting. They do not fully take Jake's perspective, but they also do not collapse Jake's mind into the reader's mind. They recognize that the rider's identity is not available inside Jake's field of view. That is better than `she`, but weaker than `he`.

The `she` answers are the revealing ones. The model has correctly inferred Lydia's gender, then projected that knowledge into Jake's utterance. It knows the story, but it does not fully model what Jake knows.

## What did we learn?

Some models, in this simple context, can preserve a character's mistaken belief. Most did not. They translated the omniscient story rather than the situated mind inside the story.

My point is not that models have limits. All do. Yes, for every LLM failure we can build a more powerful one that will succeed. Activate more weights. Give it more data. Use a different architecture. Prompt it better.

My point is to flag differences between how machines and humans learn.

Theory of mind is hard to do for machines. Important pieces of human social cognition are already visible in the first two years of life. They are not learned at university, digging through petabytes of text.

Human intelligence is complex. We cannot describe it with a handful of benchmarks in math problems, software engineering, and the like.

Pope Leo XIV puts the point more grandly in *Magnifica Humanitas*: we should resist the pretense that a single digital language can translate "the mystery of the person" into data and performance, and we should remember that the grandeur of humanity is something "no machine can ever replace." I take the same thought in a more technical register. The human condition, human dignity, and the ordinary human ability to inhabit another person's point of view are not exhausted by next-token prediction, nor by quadratic or subquadratic attention.

> **I predict Artificial Intelligence will be forever bounded away from human intelligence in at least some important dimension.**

We may not know its importance now, but we will see it when we get there.

## Further reading:

- Hu, Jennifer, Felix Sosa, and Tomer Ullman. 2025. "Re-evaluating Theory of Mind Evaluation in Large Language Models." <https://arxiv.org/abs/2502.21098>
- Gergely, György, and Gergely Csibra. 2003. "Teleological Reasoning in Infancy: The Naïve Theory of Rational Action." <https://doi.org/10.1016/S1364-6613(03)00128-1>
- Varga, Bálint, and Ágnes Melinda Kovács. 2026. "Human Infants Appreciate That Information Bears Value for Other Individuals." <https://www.nature.com/articles/s41598-025-29952-w>
- Scott, Rose M., and Renée Baillargeon. 2017. "Early False-Belief Understanding." <https://pubmed.ncbi.nlm.nih.gov/28259555/>
- Dörrenberg, Sebastian, Hannes Rakoczy, and Ulf Liszkowski. 2018. "How (Not) to Measure Infant Theory of Mind: Testing the Replicability and Validity of Four Non-Verbal Measures." <https://doi.org/10.1016/j.cogdev.2018.01.001>
- Pope Leo XIV. 2026. *Magnifica Humanitas: On Safeguarding the Human Person in the Time of Artificial Intelligence.* <https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html#Two_biblical_images>

## The experiment script

[The single .py file running the whole experiment](https://gist.github.com/korenmiklos/9b05a5b73c66c74dd865abe5bb1b230e)
