JEL codes: E03, G02\
keywords: interference; base-rate neglect; context; diagnostic expectations; recognition memory

# Introduction

Our memories of past experiences guide not only our thoughts but also our choices. We choose to save when we think about the need for future resources, or when we fear a negative shock to our wealth, and we choose to consume a specific product when positive experiences associated with that product come to mind. Whereas economic choice theories have traditionally assumed that rational agents recall the correct probability distributions associated with different states of the world, some economic models contemplate the role of memory in shaping how we construct these distributions from our record of past experiences (Bordalo et al. 2018, 2019a, 2020; Nagel and Xu 2018; Mullainathan 2002; Wachter and Kahana 2024).

Memory takes as its starting place not the rational agent, but the fundamental forces of recency, similarity, and temporal contiguity. Yet economics and psychology for many years traveled together because of a basic fact about cognition: if a pair of words, concepts, or objects frequently occur together, they will form an association, and the more they co-occur the stronger that association will be. Memory should enable agents to learn about reality, which means accurately learning conditional probability distributions. Work such as Estes ((1972), (1976)) emphasized the ability of memory theories to reproduce Bayesian findings. Among the first to question the resulting consensus was Kahneman and Tversky ((1972), (1973)) and (Tversky and Kahneman 1973), who showed, in a series of experiments, that agents do not follow Bayesian updating. The core aspect of their findings, reproduced in a tighter setting by (Bordalo et al. 2021), is that even if subjects observe many pairs $(-h,d)$, they will remember instead $(h,d)$, if they also learn $(-h,-d)$.

We explain this finding with a cognitive theory. Our work is based on the retrieved context theory of (Howard and Kahana 2002), and thus follows the basic principles of associative memory and contextual retrieval. However, their model is based on the free recall paradigm. Free recall tends to lead to the basic result observed by (Estes 1976), and also derived in (Wachter and Kahana 2024). Observations that occur more frequently will tend to be judged as having higher probability. The point of the representativeness heuristic is that this compelling intuition sometimes fails, and it fails in a predictable way. The key step in our model is treating the probabilistic judgement problem not as a process of recalling instances from memory, but rather as a flash of recognition. Think of recognition as a handshake between a cue and a target. The subject or agent determines, based on the cue, whether the cue and target go together. This determination is not based on the frequency with which they are observed together but whether they were observed under the same context. In other words, it is the similarity of the retrieved contexts that determines the recognition of an association between two objects. We model probabilistic judgement as an associative recognition problem, amenable to the same modeling tools as that well-studied experimental paradigm.

The distinction between recognition and recall is not merely terminological; it generates qualitatively different predictions. In a recall-based model, the agent samples specific episodes from memory and counts successes. Because a conjunction ($A \cap B$) is a subset of each component ($A$), any sample in which the conjunction is counted as a success also counts the component as a success, so the conjunction count can never exceed the component count. In our recognition-based model, by contrast, the agent computes a global signal---the cosine similarity of retrieved context vectors---that can, through composite representations, rate a conjunction higher than a component. Our model thus generates the *conjunction fallacy* (Tversky and Kahneman 1983), a prediction that neither probability-distortion models nor recall-based sampling models can produce. We derive the conditions under which the conjunction fallacy arises and show that it serves as a litmus test for the recognition mechanism.

To demonstrate the economic consequences of this mechanism, we develop a new application to negative stub values in equity carve-outs (Lamont and Thaler 2003). In the famous Palm/3Com episode, the market priced the subsidiary (Palm) above the parent (3Com) that owned 95% of it, implying a negative value for 3Com's non-Palm assets. Our model explains this anomaly through two complementary channels. First, Palm and 3Com retrieve different associative contexts---Palm evokes high-growth technology associations while 3Com evokes legacy-networking associations---so the market effectively prices them in different probability spaces. Second, because the states in which Palm pays off are necessarily a conjunction ("Palm does well" $\cap$ "3Com is solvent"), the conjunction fallacy predicts that investors can judge this conjunction as more probable than the component "3Com is solvent" alone, generating a negative stub value. No existing model of representativeness---whether based on probability distortion, recall, or salience-driven attention---can produce this pattern.

We also show how our theory can account for financial market anomalies such as excess volatility and the value premium.

Our paper relates to multiple strands of literature. Recent work by (Bordalo et al. 2021) casts light back to the work of (Kahneman and Tversky 1972), who conceived of non-Bayesian probabilistic judgement as arising from heuristics, one of which they termed "representativeness." Over time, representativeness appeared to merge with another heuristic, which (Tversky and Kahneman 1973) term "availability." This merging suggests that Kahneman and Tversky thought of probabilistic judgement as in part a model of memory.[^5] Their idea was that enhanced retrievability of certain instances boosts probability judgement for the category to which these instances belong. This idea that retrievability is linked with probability judgement was not unique to Tversky and Kahneman, and does not, by itself, explain the failure of Bayesian updating.

A second strand of literature is in economics and finance. Early work in behavioral finance recognized the importance of the representativeness heuristic (Barberis et al. 1998). Later, building on (Gennaioli and Shleifer 2010), (Bordalo et al. 2016) develop a model, based on a probability distortion, that can account for the key experimental finding: the mistaken application of the co-occurence of $-h$ and $-d$ (in the notation above). This model became the basis for diagnostic expectations (Bordalo et al. 2018), applied to a wide range of phenomena such as the cross-section of stock returns (Bordalo et al. 2019a), financial crises (Gennaioli and Shleifer 2018), and why aggregate real investment rates vary over time (Bordalo et al. 2019b). Nonetheless diagnostic expectations is an ad hoc model. Our model produces a cognitive explanation for the same patterns.

Our model is most closely related to that of (Bhatia 2017). Building on (Kahneman and Tversky 1972)'s basic insight that frequency judgements arise from similarity, Bhatia (2017) uses word-embedding models to create a vector representation for each word in the experiment. He then shows that similarity-based judgements match the proximity of the words to each other in a high-dimensional vector space. Frequency of word usage, as captured by the word-embedding model, determines the location of the words and their proximity. His work traces the representativeness heuristic back to information that emerges in language based on common usage. In contrast, we trace the heuristic back to a model of memory, one that is also based on proximity in a vector space. Notably, it can be used in novel situations where researchers already control for any prior language based similarities, as in (Bordalo et al. 2021). Bhatia (2017)'s results emerge as a special case of our model.

The remainder of the paper is organized as follows. Section 2 gives a formal definition of the heuristic and connects our definition with related concepts in the literature. Section 3 describes a cognitive model of the representativeness heuristic and fits data from recent experimental results. Section 4 extends the model to the conjunction fallacy. Section 5 develops a series of applications to financial markets, including negative stub values in equity carve-outs, name-change effects, stock-split anomalies, mental accounting for prices and dividends, the cross-section of stock returns, and excess volatility. Section 6 concludes.

# Defining the representativeness heuristic 

According to (Kahneman and Tversky 1972), "A person who follows \[the representativeness\] heuristic evaluates the probability of an uncertain event, or a sample, by the degree to which it is: (i) similar in essential properties to its parent population; and (ii) reflects the salient features of the process by which it is generated." Perhaps recognizing the limitations of this definition, the authors also note that representativeness is "easier to assess than to characterize." The experiments in the 1972 paper highlight misperceptions of randomness and that subjects struggle to compute posterior probabilities from sample proportions. These experiments convincingly showed that subjects depart from Bayesian reasoning, in part because they made use of settings where the Bayesian outcome was clear. However, the settings were contrived, and clearly differed from those in which people make decisions relevant to their lives using knowledge obtained from experience.

It was later, in their (1983) study, that Tversky and Kahneman wrote that what makes a hypothesis $h$ representative of data $d$ is both the co-occurence of $h$ and $d$, and the lack of co-occurence of $h$ and alternative data $-d$. The latter is fundamentally non-Bayesian. In the meantime, in (1973), the authors put forward the experiment that elucidated the concept of representativeness as it is now understood.

**Example 1** ((Kahneman and Tversky 1973)). *Subjects are given a brief description of an intelligent, organized, and introverted student and are asked to rank several fields of graduate study in order of likelihood. The subjects tend to state that the student is more likely to study computer science than the humanities, even though there are many more students in the humanities than in computer science.*

The authors asked one group of study participants to estimate the base rates of academic subjects in nine fields. A second group received a detailed description of an introverted man (Tom W.) and was asked to rank the nine fields in terms of similarity, while the third group was asked to rank the nine fields "in order of the likelihood that Tom W. is now a graduate student in each of these fields." They found a negative correlation between base rate estimates and likelihood (the opposite of what Bayesian probability computations would predict), and a near-perfect correlation between the similarity measures and the likelihood. Participants judged the base rate of humanities as far higher than that of computer science, but both the similarity and the likelihood of computer science as higher than those of the humanities.

A more recent experiment provides another example of representativeness:

**Example 2** ((Bordalo et al. 2021)). *Study participants view a sequence of images: 10 orange numbers, 15 blue numbers, and 25 blue words. When asked the likely color of an object, given that it is a number, 50% of participants say orange is the likely color.*

Crucially, both examples draw on subjects' experience of events. In the prior example, answers from the first group of participants (the group asked to estimate the base case) proxies for that experience. In the second, the experiment itself produces the experience. In neither case are the results reflective of an inability to solve a math problem, but rather capture something about everyday life.

In both cases, subjects' mistaken assessments have a *kernel of truth* (Bordalo et al. 2016). Computer science students are more likely to be introverted than the general population. In the (Bordalo et al. 2021) experiment, if an item is orange, it must be a number. However, inference by study participants goes further, to the incorrect conclusion that introverted students are more likely to study computer science, ignoring the base rate of computer science students in the population (as of the 1970s) and concluding that numbers are more likely to be orange, ignoring the base rate of blue images. However, while subjects report incorrect probabilities, their inference does not seem *that* irrational --- we can see ourselves making a similar mistake. One senses that these examples are getting at a specific cognitive deficit to which humans are subject, analogous to an optical illusion.

To formalize these notions, define the set $\Omega$ to be the population of interest. Each element of $\Omega$ consists of a pair of features (for example, being a number and being blue, or being an introvert and being a salesman). In the two experiments above, one of the elements of the pair forms the cue. Following (Bordalo et al. 2021), we refer to the set of possible cues as $\calD = \{d_1, \ldots, d_K\}$. By analogy with Bayesian updating, the cue forms the "data" on which the agent conditions. The other element of the pair is subject to retrieval based on the cue. Again following Bordalo et al. (2021), we refer to this as the *hypothesis* and denote the set of possible hypotheses by $\calH = \{h_1, \ldots, h_J\}$. Let $P$ be the physical probability measure over $\Omega = \calH\times
\calD$.

The experiment or survey asks questions pertaining to probabilities. Our theory is that subjects' answers need not reflect a probability measure in the traditional sense. The psychological theory implicit in many models of economic decision-making is that an agent carries a probability measure in their head and updates it in a manner that either approximates the laws of probability or departs from these laws in defined ways. Our view is different: the agent responds to cues, and it is the associations the agent carries in their head and updates. The laws of associations, not the mathematical laws of probability, govern the updating process. Nonetheless, it is convenient to use the notation $\Phat$ to denote elicited probabilities, keeping in mind that $\Phat$ need not have the properties of a probability measure.

We now formulate a general statement of the kernel of truth and the representativeness heuristic. Our definitions are based on those of (Bordalo et al. 2016).

**Definition 1**. *Given a physical probability measure $P$,the hypothesis-data pair $(h,d)$ exhibits the *kernel of truth* if $$
P(h|d)>P(h),

$$ or equivalently $$
P(h|d)>P(h|{-d}),

$$ where $-d$ represents $\calD\setminus\{d\}$, the elements of $\calD$ that are not equal to $d$.*

The definitions ) and ) are equivalent because $$
 P(h) = P(h|d)P(d) + P(h|{-d})P(-d).
 
$$ That is, $P(h)$ is a weighted average of $P(h|d)$ and $P(h|{-d})$. $P(h|d)$ exceeds the average, $P(h)$, if and only if it exceeds the item with which it is averaged, $P(h|{-d})$.[^6] (Bordalo et al. 2016) refer to the ratio $P(h|d)/P(h|{-d})$ as the *representativeness of data $d$ for hypothesis $h$*.

**Definition 2**. *Elicited probabilities $\Phat$ for the hypothesis-data pair $(h,d)$ exhibit the *representativeness heuristic* if $(h,d)$ exhibits the kernel of truth, and if $$
\Phat(h|d)>\Phat({-h}|d),

$$ while $$
P(h|d)\leq P({-h}|d).

$$*

An observation $d$ increases the probability of $h$ (condition )); such an observation does not go so far as to imply that $h$ is more probable than the alternative $-h$ (condition )). However, the subject states that it does (condition )). Condition ) is to rule out the less interesting case where the elicited probabilities and physical probabilities agree on the relative likelihood of $h$ and its alternative.

In Example 1, the cue $d$ is the statement that Tom is "intelligent, organized, and introverted." The hypotheses $h$ and $-h$ are that he majors in computer science or the humanities, respectively. The fact that he is introverted makes him more likely to be a computer science major than if we knew nothing about him; equivalently, computer science majors are more likely to be introverted than humanities majors. However, it does not follow that he is more likely to major in computer science than in the humanities simply because he is introverted; this ignores the base rate of humanities majors. In Example 2, 'Number' forms the cue. The hypotheses are orange and blue. The knowledge that the image is a number implies that orange is more likely than if one knew nothing. It is also the case that knowing that an image is orange implies that it must be a number. However, knowing that an image is a number does not imply that it must be orange.

The puzzle can be stated in both probabilistic and cognitive terms. Probabilistically, suppose one is attempting to measure the likelihood of hypothesis $h$ given data $d$. What one wants is the posterior probability of $h$ given $d$, and to rank this probability across various hypotheses. Because the distribution of $d$ does not matter, this is equivalent to the joint likelihood --- that is, the joint occurrence --- of $h$ and $d$. Alternatively, it corresponds to the likelihood of observing $d$ conditional on $h$, multiplied by the prior probability of $h$. In this Bayesian analysis, the distribution of $h$ conditional on $-d$ plays no role. Once the agent has computed the probability of a joint occurence of $h$ and $d$, what happens when $-d$ occurs is completely irrelevant.

In cognitive terms, a memory system that stores joint occurrences of events should retrieve the hypothesis most frequently paired with the cue. If $d$ co-occurs more often with $-h$ than with $h$, then cueing on $d$ should preferentially retrieve $-h$ rather than $h$; the strength of the $d$ and $-h$ "handshake" ought to exceed that of $d$ and $h$. Yet the data show this is not what happens: irrelevant memories associated with $-d$ contaminate the connection between $d$ and $-h$.

(Kahneman and Tversky 1972) appeal to "representativeness" and "availability": $h$ is (mistakenly) judged more probable than $-h$ because $h$ is representative of $d$. But why should $h$, and not $-h$, be representative of $d$? Why should $h$ be more available than $-h$? (Bordalo et al. 2016) noted that the key missing ingredient in the literature is the explicit role of $P(h|{-d})$, which has no normative role in Bayesian inference.

<figure data-latex-placement="h!">

<figcaption>Conditions likely to produce the representativeness heuristic. The agent observes many pairs <span class="math inline">(−<em>h</em>, <em>d</em>)</span>, represented by the dark line, and fewer pairs <span class="math inline">(<em>h</em>, <em>d</em>)</span>. Observations of <span class="math inline">−<em>h</em></span> also frequently co-occur with <span class="math inline">−<em>d</em></span>, but observations of <span class="math inline"><em>h</em></span> do not.</figcaption>
</figure>

# A cognitive theory of the representativeness heuristic 

Here, we offer a cognitive theory of the representativeness heuristic. Our theory is based on *associative recognition*, one of the main experimental paradigms in the literature on human memory (Hockley 1992; Osth and Dennis 2024).

In the associative recognition task, the subjects memorize a list of pairs. Following a delay, subjects are presented with a pair and asked if the pair was on the list. The term associative recognition arises from the need for subjects to recognize the association between one member of the pair and the other. The set of pairs presented to subjects is known as *paired associates*. Paired associates are used not only in associative recognition, but also in cued recall, in which one item of the pair cues the subject to try to recall the second item. Note that cued recall, like free recall, requires production.

At first glance, there may seem to be little relation between associative recognition and representativeness. The experiments described in Section 2 require a probabilistic judgment, not recognition of whether two items form a pair. However, we argue that this difference is merely superficial. At a deeper level, probabilistic judgment as measured by these tasks is a matter of answering the question: do two traits belong together or not?

## Model 

We start with the (Wachter and Kahana 2024) model of associations, which is ultimately based on the temporal context model of (Howard and Kahana 2002). The Howard and Kahana (2002) model accounts for data from the *free recall* task. In free recall, subjects learn a list of words and then remember the words in any order. Free recall has proven to be a highly useful paradigm in memory theory because it sheds light on how people transition from one thought to another. The literature on human learning and memory highlights three major laws: similarity, recency, and temporal contiguity. Similarity refers to the priority accorded to information that is similar to the presently active features, recency refers to priority given to recently experienced features, and temporal contiguity refers to the priority given to features that share a history of co-occurrence with the presently active features. These laws determine what information get priority in memory. Using free recall, it is possible to isolate the temporal contiguity effect: subjects exhibit better memories for items that occurred close in time to a just-recalled item. This effect, originally conjectured by Aristotle, has broad and deep empirical support.[^7]

(Wachter and Kahana 2024) model lifetime portfolio decisions. According to this model, the agent simulates future states by freely recalling prior experiences, with weights determined by present context and by the associations between features and context. In contrast, the probabilistic judgment task that is the focus of this paper is best thought of as *recognition*. Recognition and recall are distinct: recall requires production on the part of the subject; recognition does not. Recently, (Jin et al. 2024) adapt the (Howard and Kahana 2002) model to recognition memory, and show how it can explain a range of experimental phenomena. We combine elements of Jin et al. (2024) with Wachter and Kahana (2024).

While similarity, recency, and temporal contiguity are all present both in free recall and in associative recognition, they are not present to the same degree. Specifically, (Osth and Fox 2019) show that recency and temporal contiguity effects are muted in associative recognition compared with how they appear in free recall. However, subjects clearly bind a pair together in memory, suggesting a strong form of temporal contiguity intra-pair. These findings inform our modeling decisions.

As in (Wachter and Kahana 2024), the central object is the *memory matrix* $M$, a matrix of fixed dimension whose rows correspond to context states and whose columns correspond to features. The dimensions of $M$ are determined by the agent's cognitive architecture---the richness of the feature and context spaces---not by the number of experiences. Before any experiences have been encoded, $M$ may equal zero (a blank slate) or may contain pre-existing associations $M_0$ that capture prior knowledge.

Agents view features $f_i$, vectors in the feature space, together with a temporal context $x_i$, an internal mental state that evolves through time. Each experience adds an outer product to the memory matrix: $$\begin{eqnarray}
 M_n & \equiv & M_{n-1} + x_i f_{i}^\top 
 \\
& = & M_0 + \sum^n_{i = 1} x_i f_i^\top. 
\end{eqnarray}$$ Because each outer product $x_i f_i^\top$ has the same dimension as $M$, new memories are simply accumulated into the existing matrix; its size never changes.

Context, through the memory matrix, governs what comes to mind. Say that the environment presents the agent with features $f_{\textsc{ Cue}}$. These features cue context $\boldsymbol{x}_{\textsc{ Cue}}$: $$
\boldsymbol{x}_{\textsc{ Cue}}\propto M_n f_{\textsc{ Cue}},

$$ where context is determined up to a scalar multiple. Substituting ) into ) yields the following: $$
\boldsymbol{x}_{\textsc{ Cue}}\propto M_0f_{\textsc{ Cue}}+ \sum^n_{i = 1} x_i (f_i^\top f_{\textsc{ Cue}}).

$$ Equation  shows that features evoke the past contexts under which they are experienced. A context $x$ appears in the sum in ) if the corresponding $f_i$ has a positive inner product with the current feature; otherwise it does not. Thus, retrieved context is a weighted average of past contexts associated with the current feature. This basic contextual retrieval enabled the jump back in time that drove decision making in (Wachter and Kahana 2024), and it will drive probabilistic assessments in this paper.

To capture the strength of intra-pair associations and the relative lack of inter-pair associations, we assume that items viewed (nearly) simultaneously are viewed under the same context, and those viewed at different times are viewed under orthogonal contexts. To operationalize this, we assume that context only evolves if something distracts the agent. If there is no distraction, then context remains the same. If there is a distraction, by definition, that introduces orthogonal features, and context jumps to a point that is orthogonal to current context: $$
 x_{i + 1} \left\{\begin{array}{lll} = & x_i & if no distractor, \\
 \in & \{x_1,\ldots,x_i\}^\perp & otherwise. \end{array} \right.,

$$ where $\{x_1,\ldots,x_i\}^\perp$ denotes the set of vectors orthogonal to previous contexts. This assumption on contextual evolution significantly simplifies our analysis. It accounts for strong intra-pair associations because pairs of attributes, such as 'Blue' and 'Number,' occur under the same context and are retrieved together. It accounts for the relative lack of inter-pair associations, because it lacks a contextual link between pairs. If our purpose was to advance the modeling of human memory, we would retain this link at the cost of a much more complicated model, because memory data supports inter-pair contextual linkage (just less than in free recall). For this reason, (Jin et al. 2024), incorporate autoregressive context into their model.[^8] The effect of inter-pair temporal contiguity, however, is unlikely to be first-order when accounting for representativeness, which is our focus.

Allowing intra-pair characteristics to be observed under the same context solves a technical problem: how to account for objects having multiple attributes (for example, being both blue and a number). In our framework, 'Blue' and 'Number' form a pair which subjects learn, in a similar manner to learning pairs of words in the associative recognition task. For simplicity, we treat 'Blue' and 'Number' as orthogonal feature vectors. Subjects build a *composite representation* (Metcalfe 1991) using autoregressive context. The only similarity in the model comes through items sharing a context.

In the (Jin et al. 2024), extension of the (Howard and Kahana 2002) model, whether recognition occurs or not depends on *contextual similarity*. The cue $f_{\textsc{ Cue}}$ retrieves context $\boldsymbol{x}_{\textsc{ Cue}}$, ). To recognize an association, the agent considers the context retrieved by target feature $f_{\textsc{ Target}}$: $$\boldsymbol{x}_{\textsc{ Target}}\propto Mf_{\textsc{ Target}}$$ (suppressing the subscript $n$). The agent compares these retrieved contexts based on their inner products to some threshold criterion $c_{\rm recog}\in (0,1)$: $$
\boldsymbol{x}_{\textsc{ Cue}}\cdot \boldsymbol{x}_{\textsc{ Target}}> c_{\rm recog}

$$ (Stanislaw and Todorov 1999). If the inner product exceeds the threshold, the cue and target are recognized as a pair. If there are two targets, as is the case with the representativeness heuristic, the one with the higher inner product is the one the agent chooses as the match. Retrieved contexts are scaled so as to be norm 1 according to the standard Euclidean ($L^2$) norm, implying that the inner product is equivalent to cosine similarity (we discuss the choice of norm below). In Section 3.4, we generalize the model to allow an error term to combine with ) to determine recognition. We now summarize the model.

**Model Summary 1**. *Suppose an agent views $n$ elements of $\calH\times \calD$ as feature vectors $f_i,$ $i =
1,\ldots, n$. That is, $f_i$ is a composite representation $$
f_i = f_h + f_d, \quad h\in \calH, d\in \calD,

$$ where, for simplicity, $f_h$ and $f_d$ are orthogonal vectors. Feature vectors $f_i$ combine with orthogonal contexts $x_i$ to form memory $M$ as in ), with $M_0$ the zero matrix. Let $f_\mathcal{j},$ $\mathcal{j}\in \calH\cup \calD$, represent either a cue ($d\in \calD$) or a target ($h\in \calH$). When cued with $d$, the agent recognizes target $h$ as more likely than some other target $-h$ if $$\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d > \boldsymbol{x}_{-h} \cdot \boldsymbol{x}_d$$ where $\boldsymbol{x}_\mathcal{j},$ $\mathcal{j}\in \calH\cup \calD$, is a norm-1 retrieved context vector such that $\boldsymbol{x}_{\mathcal{j}} \propto M
f_{\mathcal{j}}$.*

To understand how this model accounts for the representativeness heuristic, consider the following simplified version of Example 2. There is a list of three elements: a blue number 5, an orange number 3, and a blue word 'CAT.' Each becomes embedded in its own context: $$\begin{array}{cccc}
'5' & - & Blue & \leftrightarrow x_1 \\
'3' & - & Orange & \leftrightarrow x_2 \\
'CAT' & - & Blue & \leftrightarrow x_3
\end{array}$$

We model these items in the feature space as follows: $$\begin{array}{cccc}
\textsc{Number} & \textsc{Word} & \textsc{Blue} & \textsc{Orange} \\ 
~\\
\updownarrow &\updownarrow & \updownarrow & \updownarrow\\
~\\
\myvectoriv{1}{0}{0}{0}& \myvectoriv{0}{1}{0}{0}& \myvectoriv{0}{0}{1}{0}& \myvectoriv{0}{0}{0}{1}
\end{array}$$

The following represents how features are bound together with context in a participant's mental representation of the list: $$
\begin{array}{ccccc}
Blue '5' & // & Orange '3' & // & Blue 'CAT' \\
 \underbrace{\myvectoriv{0}{0}{1}{0}, \myvectoriv{1}{0}{0}{0}}_{ } & & \underbrace{\myvectoriv{0}{0}{0}{1}, \myvectoriv{1}{0}{0}{0}}_{ } & & \underbrace{\myvectoriv{0}{0}{1}{0}, \myvectoriv{0}{1}{0}{0}}_{ }\\
x_1 & & x_2 & & x_3 \\
\myvectoriii{1}{0}{0}& & \myvectoriii{0}{1}{0}& & \myvectoriii{0}{0}{1}
\end{array}

$$ and this results in the memory matrix $$\begin{eqnarray}
M_n & = & M_0 + \sum^n_{i = 1} x_i f_i^\top \\
& = & M_0+ \myvectoriii{1}{0}{0}\left(\myvectoriv{0}{0}{1}{0}+ \myvectoriv{1}{0}{0}{0}
 \right)^\top\!\!\!\!
+
 \myvectoriii{0}{1}{0}\left(\myvectoriv{0}{0}{0}{1}+ \myvectoriv{1}{0}{0}{0}\right)^\top
\!\!\!\!+
 \myvectoriii{0}{0}{1}
\left(
 \myvectoriv{0}{0}{1}{0}+ \myvectoriv{0}{1}{0}{0}\right)^\top \\
& = & M_0 + \myvectoriii{1}{0}{0}
\!\begin{array}{c}[\,1 \ \ 0 
 \ \ 1 \ \ 0\,]\\ ~ \\
 ~\end{array} +
 \myvectoriii{0}{1}{0}\!\begin{array}{c}[\,1 \ \ 0 
 \ \ 0 \ \ 1\,]\\ ~ \\
 ~\end{array} +
 \myvectoriii{0}{0}{1}\!\begin{array}{c}[\,0 \ \ 1 
 \ \ 1 \ \ 0\,]\\ ~ \\
 ~\end{array}

\end{eqnarray}$$ We abstract away from pre-experimental associations by setting all elements of $M_0$ to zero. Then, suppressing subscripts,[^9] $$
M = \begin{bmatrix}
1 & 0 & 1 & 0\\
1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0
\end{bmatrix}.

$$

The cue is the feature 'Number,' which retrieves context $$
\boldsymbol{x}_{\textsc{ Number}}\equiv \frac{Mf_{\textsc{ Number}}}{||Mf_{\textsc{ Number}}||} \propto M \myvectoriv{1}{0}{0}{0}= \myvectoriii{1}{1}{0} \propto
\myvectoriii{1/\sqrt{2}}{1/\sqrt{2}}{0}.

$$ Targets are 'Blue' and 'Orange': $$
\boldsymbol{x}_{\textsc{ Blue}}\equiv \frac{Mf_{\textsc{ Blue}}}{||Mf_{\textsc{ Blue}}||} \propto \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
\propto \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$ and $$
\boldsymbol{x}_{\textsc{ Orange}}\equiv \frac{Mf_{\textsc{ Orange}}}{||Mf_{\textsc{ Orange}}||} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} .
$$ Note how $$\begin{array}{ccc}
 \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Orange}}& > & \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Blue}}\\
 \mathrel{$=$}& & \mathrel{$=$}\\
 1/\sqrt{2} & & 1/2
 \end{array}$$ Because the context of 'Number' more closely resembles that of 'Orange,' the participant reports 'Orange' as the more likely color. The presence of the blue words, in effect, drives out the memory of the blue numbers.

Before stating general properties of the model, we develop intuition with two additional examples. First, we consider a list that adds one more blue number. When we lengthen the "experiment" above by one blue number, we add one more row to the block of $M$ that we are considering: $$M = \begin{bmatrix}
1 & 0 & 1 & 0\\
1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0
\end{bmatrix}.$$ Now, the following retrieved contexts are $$\begin{eqnarray*}
 \boldsymbol{x}_{\textsc{ Blue}}\propto \begin{bmatrix} 1 \\ 0 \\ 1 \\ 1\end{bmatrix}
 \propto \begin{bmatrix} 1/\sqrt{3} \\ 0 \\ 1/\sqrt{3} \\
 1/\sqrt{3}\end{bmatrix}, \quad
 \boldsymbol{x}_{\textsc{ Orange}}= \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}
\end{eqnarray*}$$ whereas $$\boldsymbol{x}_{\textsc{ Number}}\propto \begin{bmatrix} 1 \\ 1 \\ 0 \\ 1\end{bmatrix}
\propto \begin{bmatrix} 1/\sqrt{3} \\ 1/\sqrt{3} \\ 0 \\ 1/\sqrt{3}\end{bmatrix}$$ We see that $$\begin{array}{ccc}
 \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Blue}}& >& \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Orange}}\\
 \mathrel{$=$}& & \mathrel{$=$}\\
 2/3 & & 1/\sqrt{3}
\end{array}$$ This example suggests that inner products have the reasonable property that, as instances of a pair increase, the likelihood of recognition, as measured by the inner product, also increases.

Second, we replace the blue words with gray shapes. In the (Bordalo et al. 2021) experiment, the effect disappears. A simple calculation explains why. We first add a feature vector, $$\begin{array}{ccccc}
\textsc{Number} & \textsc{Shape} & \textsc{Blue} & \textsc{Orange} & \textsc{Gray}\\ 
~\\
\updownarrow &\updownarrow & \updownarrow & \updownarrow & \updownarrow\\
~\\
\begin{bmatrix}1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}& \begin{bmatrix}0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}& \begin{bmatrix}0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}& \begin{bmatrix}0 \\ 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}& \begin{bmatrix}0 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}
\end{array}$$ and then assume the following simple list: $$
\begin{array}{ccccc}
Blue '5' & // & Orange '3' & // & Gray \square\\
 \underbrace{\begin{bmatrix}0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix}1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}}_{ } & &
 \underbrace{\begin{bmatrix}0 \\ 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix}1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}}_{ } & &
 \underbrace{\begin{bmatrix}0 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}, \begin{bmatrix}0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}}_{ }\\
x_1 & & x_2 & & x_3 \\
\myvectoriii{1}{0}{0}& & \myvectoriii{0}{1}{0}& & \myvectoriii{0}{0}{1}
\end{array}

$$ Applying the same reasoning as in ) implies that the memory matrix equals $$
M = \begin{bmatrix}
1 & 0 & 1 & 0 & 0\\
1 & 0 & 0 & 1 & 0\\
0 & 1 & 0 & 0 & 1
\end{bmatrix}

$$ 'Number' again forms the cue. The cue retrieves the context ). The targets are each of the two possible colors. Each color retrieves a basis vector context: $$\boldsymbol{x}_{\textsc{ Blue}}= \begin{bmatrix} 1 \\ 0 \\ 0
 \end{bmatrix}, \quad \boldsymbol{x}_{\textsc{ Orange}}= \begin{bmatrix} 0 \\ 1 \\
 0 \end{bmatrix}, \quad \boldsymbol{x}_{\textsc{ Gray}}= \begin{bmatrix} 0 \\ 0 \\ 1\end{bmatrix}$$ The inner product with the context vector $\boldsymbol{x}_{\textsc{ Number}}$ now gives the correct ranking --- namely, equal likelihood for blue and orange.

Retrieved context theory, combined with the tools of recognition memory, offers an entirely novel hypothesis. Likelihoods arise from associative strengths in memories retrieved in response to a cue. The agent looks directly at the similarity to the latent context evoked by the cue. Probabilities do not emerge from the process of recall, but rather from an instant of recognition.

The assumptions we have made above are not innocuous. There are situations where previous experience, captured in $M_0$ becomes important. One place is in creating subject-specific variation, which we incorporate below through a noise term. A second case arises when one of the targets is a better match for previous associations than for the list. For example, (Bordalo et al. 2023) present subjects with two lists, one containing animals and names and the other containing animals and other heterogeneous words. In both cases, the animals made up 40% of the list. Subjects are then asked, as in the Example 2 above, "Suppose the computer randomly chose a word from the words you just saw. What is the percent chance that it is an animal?" They show that subjects report a significantly higher probability that the word is an animal when the list contains animals and names versus when the list contains animals and heterogenous words. If the cue is "word on the list," then "animal" and "name" are approximately equally good targets. On the other hand, the target "heterogeneous words" would most likely be a greater match for a prior list context, which in our model would be captured by pre-existing associations in $M_0$.

## Properties

We now formally prove the properties suggested by the simple examples above.

**Theorem 1**. *Suppose that the agent views an unbiased sample of elements of $\calH\times
\calD$. Assuming the cognitive process described in the 1, the agent ranks the relative probability of targets $h\in\calH$ given cue $d\in \calD$ according to: $$\begin{eqnarray}
 \boldsymbol{x}_h\cdot \boldsymbol{x}_d & = & \frac{P(h,d)}{\sqrt{P(h)P(d)}} \\
 & \propto & \frac{P(h,d)}{\sqrt{P(h,d) + P(h,-d)}}. 
\end{eqnarray}$$ Thus, for elements $h,{-h}\in\calH$, inner products satisfy $$
\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d > \boldsymbol{x}_{-h}\cdot
\boldsymbol{x}_d

$$ if and only if $$
 P(h|d) >P(-h|d) \sqrt{\frac{P(h)}{P(-h)}}.
 
$$ In the case where $\calH = \{h, {-h}\}$, namely $\calH$ consists of only two elements, inner products satisfy ) if and only if $$
 P(h|d) >P({-h}|d) \sqrt{\frac{P(h)}{1-P(h)}}.
 
$$*

*Proof.* It follows from ) and the features definition ) that, when cued by $f_\mathcal{j}, \mathcal{j}\in
\calH \cup \calD$, $$\boldsymbol{x}_{\mathcal{j}} \propto M f_\mathcal{j}\propto \sum_{i = 1}^n x_i\mathbb{1}_{f_{i}^\top
 f_\mathcal{j}= 1},$$ where $x_i$ is context as of time $i$. For a given $\mathcal{j}$, there are $\#\{i : f_{i}^\top
 f_\mathcal{j}= 1\}$ nonzero elements of $\boldsymbol{x}_{\mathcal{j}}$, equal to the number of occurrences of primary features vector $f_{\mathcal{j}}$ in the sample. Because context lies on the unit circle, $\boldsymbol{x}_{\mathcal{j}}$ is the unit vector with nonzero entries corresponding to locations in the list or time in the sample when elements of $\mathcal{j}$ are observed: $$\boldsymbol{x}_\mathcal{j}(i) = \frac{1}{\sqrt{\#\{ i : f_i^\top
 f_\mathcal{j}= 1\} }} \times \left\{\begin{array}{c}1 \quad f_i^\top f_\mathcal{j}= 1, \\ 0 \quad otherwise. \end{array}\right.$$

Now consider the inner product $\boldsymbol{x}_\mathcal{j}\cdot
\boldsymbol{x}_{\mathcal{k}}$: the sum of products of entries of $\boldsymbol{x}_{\mathcal{j}}$ and $\boldsymbol{x}_{\mathcal{k}}$. These are entries of ones and zeros scaled by the square root of the number of non-zero entries. Thus $$\begin{eqnarray*}
\boldsymbol{x}_\mathcal{j}\cdot \boldsymbol{x}_{\mathcal{k}} & = & \#\{ i :
 (f_{i}^\top
 f_\mathcal{j}\neq 0) \, \&\,
(f_{i}^\top f_{\mathcal{k}} \neq 0)\} \times \frac{1}{\sqrt{\#\{i : f_{i}^\top
 f_\mathcal{j}= 1\} } }\frac{1}{\sqrt{\# \{i : f_{i}^\top
 f_\mathcal{k}= 1\} } } \\
& = & P(\mathcal{j}, \mathcal{k})n \times
 \frac{1}{\sqrt{P(\mathcal{j})n}}\frac{1}{\sqrt{P(\mathcal{k})n}}.
\end{eqnarray*}$$ Dividing both the numerator and the denominator by $n$ gives the relative frequency in the observed sample. Assuming the frequency in the observed sample equals the population density yields ).

Finally, ) follows from $$P(h)P(d) =( P(h,d) + P(h,-d))P(d),$$ and dropping the constant of proportionality $1/\sqrt{P(d)}$. Equation ) follows from applying ) to both sides of ) and rearranging. ◻

Theorem 1 has a geometric interpretation. Because context vectors are unit 1, the inner product is the cosine of the angle between the vectors. If the vectors lie on top of each other, this corresponds to the case in which $\mathcal{j}$ and $\mathcal{k}$ are always seen together. When they are never seen together, the vectors are orthogonal, and everything else lies somewhere in between. See, for example, Figure 1. In Panel (a), the context vectors are orthogonal and therefore have zero cosine similarity. In Panel (b), the similarity of the contexts is captured by the fact that the angle between them is smaller, implying a higher cosine similarity.

<figure id="fig:angles" data-latex-placement="htbp">
<figure>

<figcaption>Orthogonal contexts</figcaption>
</figure>
<figure>

<figcaption>Associated contexts</figcaption>
</figure>
<figcaption>Geometric interpretation of cosine similarity between context vectors.</figcaption>
</figure>

An immediate consequence of this theorem is how likelihood judgments depend on the probability distribution viewed by the agent. We first ask what happens when, conditional on $d$, $h$ becomes more likely, holding fixed the distribution of $d$ and the conditional probability of $h$ given $-d$, where $-d$ should be understood as any element of $\calD$ not equal to $d$.

The first statement below says that if $h$ is judged to be more likely than $-h$, and more evidence accumulates in favor of $h$ in the sense that $P(h|d)$ rises, then $h$ will be judged as still more likely than $-h$ when cued by $d$. This is in line with Bayesian reasoning. The second statement says that if $h$ is considered more likely than $-h$, and evidence accumulates that reduces the probability of $h$ conditional on $-d$, then $h$ will be considered as still more likely than $-h$ when cued by $d$. This is contrary to Bayesian reasoning.[^10]

**Theorem 2**. *Suppose that pairs of features are observed in proportion to probabilities $P(\cdot)$, resulting in $\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d>\boldsymbol{x}_{-h}\cdot
 \boldsymbol{x}_d$ for some $h,{-h}\in\calH$. Assume a new set of feature pairs are observed, updating probabilities to $P'(\cdot)$ such that*

1. *$P'(h|d)>P(h|d)$ but with $P(d)$ and $P(\cdot|{-d})$ unchanged, and with $P({-h}|d)$ either falling or remaining the same; or*

2. *$P'(h|{-d})<P(h|{-d})$ but with $P(d)$ and $P(\cdot|{d})$ unchanged, and with $P({-h}|{-d})$ either increasing or remaining the same.*

*Then, if $\boldsymbol{x}'$ represents the new retrieved context: $$
\boldsymbol{x}_h'\cdot \boldsymbol{x}_d' >\boldsymbol{x}_h\cdot
\boldsymbol{x}_d>\boldsymbol{x}_{-h}\cdot
\boldsymbol{x}_d\geq\boldsymbol{x}'_{-h}\cdot \boldsymbol{x}'_d

$$*

*Proof.* Because we are only concerned about the relative ranking of $\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d$ and $\boldsymbol{x}_{-h}\cdot
 \boldsymbol{x}_d$, it suffices to consider ), which we can rewrite as: $$\begin{eqnarray}
\boldsymbol{x}_h \cdot \boldsymbol{x}_d & \propto & \frac{P(h|d)P(d)}{\sqrt{P(h|d)P(d)
 + P(h|{-d})P({-d})}} \\ 
& \propto & \sqrt{\frac{P(h|d)}{P(d)
 + (P(h|{-d})/P(h|d))P(-d)}} 
\end{eqnarray}$$ which is increasing in $P(h|d)$ and decreasing in of $P(h|{-d})$.

Suppose the first condition in the theorem holds. $P'(h|d)>P(h|d)$ implies $$\begin{eqnarray*}
\sqrt{\frac{P'(h|d)}{P'(d)
 + (P'(h|{-d})/P'(h|d))P'({-d})}} & = & \sqrt{\frac{P'(h|d)}{P(d)
 + (P(h|{-d})/P'(h|d))P({-d})}} \\ & >& \sqrt{\frac{P(h|d)}{P(d)
 + (P(h|{-d})/(P(h|d))P({-d})}} ,
\end{eqnarray*}$$ where the equality follows from the assumption that $P(d)$ and $P(h|{-d})$ remain unchanged, and the inequality follows from the fact that ) is increasing in $P(h|d)$. This shows $\boldsymbol{x}'_{h}\cdot \boldsymbol{x}'_d>\boldsymbol{x}_h\cdot
 \boldsymbol{x}_d$. Moreover, because we have assumed that $P'({-h}|d)\leq P({-h}|d)$ for hypothesis ${-h}\in\calH$, similar reasoning implies $$\begin{eqnarray*}
\sqrt{\frac{P'({-h}|d)}{P'(d)
 + (P'({-h}|{-d})/P'({-h}|d))P'({-d})}} & = & \sqrt{\frac{P'({-h}|d)}{P(d)
 + (P({-h}|{-d})/P'({-h}|d))P({-d})}} \\ & \leq& \sqrt{\frac{P({-h}|d)}{P(d)
 + (P({-h}|{-d})/(P({-h}|d))P({-d})}} ,
\end{eqnarray*}$$ so $\boldsymbol{x}_{-h}\cdot \boldsymbol{x}_d\geq \boldsymbol{x}'_{-h}\cdot \boldsymbol{x}'_d$. Putting these together, we have ).

Now suppose instead that the second condition in the theorem holds. $P'(h|{-d})<P(h|{-d})$ implies $$\begin{eqnarray*}
\sqrt{\frac{P'(h|d)}{P'(d)
 + (P'(h|{-d})/P'(h|d))P'({-d})}} & = & \sqrt{\frac{P(h|d)}{P(d)
 + (P'(h|{-d})/P(h|d))P({-d})}} \\ & >& \sqrt{\frac{P(h|d)}{P(d)
 + (P(h|{-d})/(P(h|d))P({-d})}} ,
\end{eqnarray*}$$ where the first equality follows from the assumption that $P(d)$ and $P(h|d)$ remain unchanged, and the second follows from the fact that ) is decreasing in $P(h|{-d})$. This shows $\boldsymbol{x}'_{h}\cdot \boldsymbol{x}'_d>\boldsymbol{x}_h\cdot
 \boldsymbol{x}_d$. Moreover, because we have assumed that $P'({-h}|{-d})\geq P({-h}|{-d})$ for hypothesis ${-h}\in\calH$, similar reasoning implies $$\begin{eqnarray*}
\sqrt{\frac{P'({-h}|d)}{P'(d)
 + (P'({-h}|{-d})/P'({-h}|d))P'({-d})}} & = & \sqrt{\frac{P({-h}|d)}{P(d)
 + (P'({-h}|{-d})/P({-h}|d))P({-d})}} \\ & \leq& \sqrt{\frac{P({-h}|d)}{P(d)
 + (P({-h}|{-d})/(P({-h}|d))P({-d})}} ,
\end{eqnarray*}$$ so $\boldsymbol{x}_{-h}\cdot \boldsymbol{x}_d\geq \boldsymbol{x}'_{-h}\cdot \boldsymbol{x}'_d$. Putting these together, we have ). ◻

We can also show that, given sufficient evidence of $h$ conditional on $d$, the agent will rank the likelihood of $h$ above any alternatives when cued with $d$. This is consistent with Bayesian reasoning.

**Theorem 3**. *Keeping $P(d)$ and $P(h|{-d})$ fixed, for $P(h|d)$ sufficiently close to 1, $\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d>\boldsymbol{x}_{-h}\cdot
 \boldsymbol{x}_d$.*

*Proof.* Suppose that the statement were false. Then there is a sequence of samples, indexed by $n$, such that as $P^{(n)}(h|d)$ approaches 1, the inequality is violated. Consider a subsequence such that $P^{(n)}(h|d)$ monotonically approaches 1, and simultaneously $P^{(n)}(-h|d)$ monotonically approaches zero. The latter is possible because $P(-h|d)\leq 1- P(h|d)$, and is bounded below by zero. It follows from ) that $$\begin{eqnarray*}
\lim_{n\rightarrow\infty} \frac{\boldsymbol{x}^{(n)}_{-h}\cdot \boldsymbol{x}^{(n)}_d}{\boldsymbol{x}^{(n)}_{h}\cdot 
 \boldsymbol{x}^{(n)}_d} & = & \lim_{n\rightarrow\infty} 
 \frac{P^{(n)}(-h,d)}{\sqrt{P^{(n)}(-h)}}\frac{\sqrt{P^{(n)}(h)}}{P^{(n)}(h,d)}\\
& = & \lim_{n\rightarrow\infty}
 \sqrt{\frac{P^{(n)}(h)}{P^{(n)}(-h)}}\frac{P^{(n)}(-h|d)}{P^{(n)}(h|d)}
 \\
 & = &
 \lim_{n\rightarrow\infty}\sqrt{\frac{P^{(n)}(h)}{P^{(n)}(-h)}}
 \lim_{n\rightarrow\infty}\frac{P^{(n)}(-h|d)}{P^{(n)}(h|d)}
 = 0
\end{eqnarray*}$$ The last line follows because the limits of both terms are well-defined because $P(-h|-d)$ is unchanged. Moreover, $\frac{P^{(n)}(-h|d)}{P^{(n)}(h|d)}$ decreases monotonically to zero, whereas $\sqrt{\frac{P^{(n)}(h)}{P^{(n)}(-h)}}$ is bounded. Therefore, there exists an $N$ such that $\frac{\boldsymbol{x}^{(n)}_{-h}\cdot \boldsymbol{x}^{(n)}_d}{\boldsymbol{x}^{(n)}_{h}\cdot 
 \boldsymbol{x}^{(n)}_d}<1$ for $n> N$, which is a contradiction. ◻

However, if $h$ becomes sufficiently associated with $-d$, then the agent will rank $h$ below any of the alternatives, inconsistent with Bayesian reasoning.

**Theorem 4**. *Keeping $P(\cdot|d)$ fixed (with $P({-h}|d)>0$), for $P(h)$ sufficiently close to 1, $\boldsymbol{x}_{h}\cdot \boldsymbol{x}_d<\boldsymbol{x}_{-h}\cdot
 \boldsymbol{x}_d$.*

*Proof.* Suppose that the statement were false. Then there is a sequence of samples, indexed by $n$, such that as $P^{(n)}(h)$ monotonically approaches 1 and $P^{(n)}(-h)$ monotonically approaches zero, the inequality is violated. It follows from ) that $$\begin{eqnarray*}
\lim_{n\rightarrow\infty} \frac{\boldsymbol{x}^{(n)}_{h}\cdot \boldsymbol{x}^{(n)}_d}{\boldsymbol{x}^{(n)}_{-h}\cdot 
 \boldsymbol{x}^{(n)}_d} & = & \lim_{n\rightarrow\infty} 
 \frac{P^{(n)}(h,d)}{\sqrt{P^{(n)}(h)}}\frac{\sqrt{P^{(n)}(-h)}}{P^{(n)}(-h,d)}\\
& = & \lim_{n\rightarrow\infty}
 \sqrt{\frac{P^{(n)}(-h)}{P^{(n)}(h)}}\frac{P^{(n)}(h|d)}{P^{(n)}(-h|d)}
 \\
 & = &
 \lim_{n\rightarrow\infty}\sqrt{\frac{P^{(n)}(-h)}{P^{(n)}(h)}}
 \lim_{n\rightarrow\infty}\frac{P^{(n)}(h|d)}{P^{(n)}(-h|d)}
 = 0
\end{eqnarray*}$$ The last line follows because both terms are well-defined, and indeed $\frac{P^{(n)}(h|d)}{P^{(n)}(-h|d)}$ is constant. Moreover, $\sqrt{\frac{P^{(n)}(-h)}{P^{(n)}(h)}}$ monotonically decreases to zero. Therefore, there exists an $N$ such that $\frac{\boldsymbol{x}^{(n)}_{h}\cdot \boldsymbol{x}^{(n)}_d}{\boldsymbol{x}^{(n)}_{-h}\cdot 
 \boldsymbol{x}^{(n)}_d}<1$ for $n> N$, which is a contradiction. ◻

For example, consider Example 2. $P(\textsc{ Orange})n$ is the count of orange items in the list, and $P(\textsc{ Orange},\textsc{ Number})n$ is the count of orange numbers. Feature $\textsc{ Orange}$ will retrieve a context vector with $P(\textsc{ Orange})n$ nonzero elements. Because the context vector must have norm 1, each of these elements equals $1/\sqrt{P(\textsc{ Orange})n}$. Analogous results hold true for feature $\textsc{ Number}$. Now consider the inner product of these two context vectors. Because the inner product sums the nonzero elements, of which there are at most $\min(P(\textsc{ Number}),P(\textsc{ Orange}))n$. In this example, there are exactly $P(\textsc{ Orange})n$ nonzero elements, not only because there are fewer orange items, but because all orange items are numbers. If there were some orange items that were not numbers, the context overlap would be less than perfect, and there would be fewer than $P(\textsc{ Orange})n$ nonzero elements. Regardless, the number of nonzero elements scales with $n$. Thus, the inner product does not depend on $n$. In the specific case of orange numbers, the inner product equals $P(\textsc{ Orange},\textsc{ Number})/\sqrt{P(\textsc{ Number})P(\textsc{ Orange})}$, where $P(\textsc{ Orange},\textsc{ Number})$ is the joint likelihood of orange and number.

The discussion in this section highlights the importance of using $L^2$ scaling, namely, the standard Euclidean norm. If we were to use $L^1$ scaling, the inner product would actually fall with the sample size, a counterintuitive result. Each of the elements in the context vector associated with feature $\textsc{ Orange}$ would equal $1/(P(\textsc{ Orange})n)$, whereas each item in the context vector associated with $\textsc{ Number}$ equals $1/(P(\textsc{ Number})n)$. The inner product would equal $P(\textsc{ Number},\textsc{ Orange})/(n\sqrt{P(\textsc{ Number})P(\textsc{ Orange})})$, a decreasing function of $n$. While one could redefine cognitive processes through cosine similarity (namely, use not the inner product but the scaled inner product), and thus recover the same result under context vectors scaled under the $L^1$ norm, such an approach introduces an extra step without adding explanatory power.

## Qualitative results 

We first show that this model fits the results of (Bordalo et al. 2021), Study 1 of which forms the basis of Example 2 above. In this experiment, associations are formed only during the presentation of the items, ruling out the possibility that the subject learned biased conditional probabilities outside of the experiment. This controlled setting also allows the experimenter to vary the number of targets and decoys and assess how this affects likelihood judgments. For these reasons, we emphasize the results in this study when we fit the model to the data. We first examine the qualitative predictions of the model.

To control for possible differences in the mental database for orange and blue, Bordalo et al. (2021) randomly assign participants to one of two treatments. Each participant sees a sequence of 50 of these abstract images. In the first condition, they see 10 orange numbers, 15 blue numbers, and 25 gray shapes (*gray* treatment). In the second condition, they see 10 orange numbers, 15 blue numbers, and 25 blue words (the *blue* treatment). Participants are then asked "An image was randomly drawn from the images that were just shown to you. The chosen image showed a number. What is the likely color of the chosen image?" They find the following two results:

1. Participants are significantly more likely to say that orange is the more likely color in the blue treatment versus the gray treatment.[]

2. The percentage of participants who say that orange is the most likely color declines with $k$, as $k$ blue words are replaced with $k$ orange words. 

(Bordalo et al. 2021) also ask questions regarding the probability and number of orange words. Appendix 7 shows how the model can be extended to handle probabilistic questions, and then shows that our model matches results analogous to Results  and  for probability judgments.

Table 1 illustrates the mapping between this setting and our model. The cue $d=\textsc{ Number}$ and the decoy $-d$ is shape in the gray treatment and word in the blue treatment. The targets are the colors $h=\textsc{ Orange}$ and $-h=\textsc{ Blue}$.[^11]

At the beginning of this section, we showed how the model can produce differential results for the blue versus gray treatment in a toy example. We now use the numbers from the (Bordalo et al. 2021) experiment. We find, for the gray treatment, $$\begin{eqnarray*}
\boldsymbol{x}_{\textsc{ Blue}}\cdot \boldsymbol{x}_{\textsc{ Number}}& = & \frac{P_g(\textsc{ Blue},\textsc{ Number})}{\sqrt{P_g(\textsc{ Blue})P_g(\textsc{ Number})}} =
 \frac{15}{\sqrt{15}\sqrt{15+10}} = 0.77 \\
\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{ Number}}& = & \frac{P_g(\textsc{ Orange},\textsc{ Number})}{\sqrt{P_g(\textsc{ Orange})P_g(\textsc{ Number})}} =
 \frac{10}{\sqrt{10}\sqrt{15+10}} = 0.63
\end{eqnarray*}$$ Under the gray treatment, the agent correctly recalls a greater likelihood that the number is blue.

In contrast, in the blue treatment, $$\begin{eqnarray*}
\boldsymbol{x}_{\textsc{ Blue}}\cdot \boldsymbol{x}_{\textsc{ Number}}& = & \frac{P_b(\textsc{ Blue},\textsc{ Number})}{\sqrt{P_b(\textsc{ Blue})P_b(\textsc{ Number})}} =
 \frac{15}{\sqrt{15+25}\sqrt{15+10}} = 0.47 \\
\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{ Number}}& = & \frac{P_b(\textsc{ Orange},\textsc{ Number})}{\sqrt{P_b(\textsc{ Orange})P_b(\textsc{ Number})}} =
 \frac{10}{\sqrt{10}\sqrt{15+10}} = 0.63
\end{eqnarray*}$$ The introduction of blue words weakens the association between the color blue and numbers, so that, under the blue treatment, the agent incorrectly recalls a greater likelihood of the number being orange: $$P_b(\textsc{ Orange}|\textsc{ Number}) > P_b(\textsc{ Blue}|\textsc{ Number})\sqrt{\frac{P_b(\textsc{ Orange})}{P_b(\textsc{ Blue})}}.$$ However, $$P_g(\textsc{ Orange}|\textsc{ Number}) < P_g(\textsc{ Blue}|\textsc{ Number})\sqrt{\frac{P_g(\textsc{ Orange})}{P_g(\textsc{ Blue})}}. 
$$

To build intuition regarding Result , we add an orange word to our toy model from Section 3.1: $$\begin{array}{cccc}
'5' & - & Blue & \leftrightarrow x_1 \\
'3' & - & Orange & \leftrightarrow x_2 \\
 'CAT' & - & Blue & \leftrightarrow x_3\\
 'DOG' & - & Orange & \leftrightarrow x_4
\end{array}$$ The list becomes: $$
\begin{array}{ccccccc}
Blue '5' & // & Orange '3' & // & Blue 
 'CAT' & // & 
 Orange
 
 'DOG'\\
 \underbrace{\myvectoriv{0}{0}{1}{0}, \myvectoriv{1}{0}{0}{0}}_{ } & &
 \underbrace{\myvectoriv{0}{0}{0}{1},\myvectoriv{1}{0}{0}{0}}_{ } & & \underbrace{\myvectoriv{0}{0}{1}{0},\myvectoriv{0}{1}{0}{0}}_{ }
& & \underbrace{\myvectoriv{0}{0}{0}{1},\myvectoriv{0}{1}{0}{0}}_{ }
 \\
x_1 & & x_2 & & x_3 & & x_4\\
\myvectoriv{1}{0}{0}{0}& & \myvectoriv{0}{1}{0}{0}& & \myvectoriv{0}{0}{1}{0}& & \myvectoriv{0}{0}{0}{1}
\end{array}

$$ Following the reasoning of ), we have: $$M = \myvectoriv{1}{0}{0}{0}\!\begin{array}{c}[\,1 \ \ 0 
 \ \ 1 \ \ 0\,]\\ ~ \\~\\
 ~\end{array} \!\! + \, \,\myvectoriv{0}{1}{0}{0}
\!\begin{array}{c}[\,1 \ \ 0 
 \ \ 0 \ \ 1\,]\\ ~ \\~\\
 ~\end{array} \!\! + \, \,\myvectoriv{0}{0}{1}{0}\!\begin{array}{c}[\,0 \ \ 1 
 \ \ 1 \ \ 0\,]\\ ~ \\~\\
 ~\end{array} \!\!+\,\,
\myvectoriv{0}{0}{0}{1}\!\begin{array}{c}[\,0 \ \ 1 
 \ \ 0 \ \ 1\,]\\ ~ \\~\\
 ~\end{array}$$ Note that the first three rows of $M$ are the same as what we had before adding an orange word. $$
M= \begin{bmatrix}
1 & 0 & 1 & 0\\
1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0 \\
0 & 1 & 0 & 1
\end{bmatrix}.

$$ As in Study 1, participants are asked "What is the likely color of the number?" The cue, feature 'Number,' retrieves context $$
\boldsymbol{x}_{\textsc{ Number}}\propto M \myvectoriv{1}{0}{0}{0}= \myvectoriv{1}{1}{0}{0} \propto
\myvectoriv{1/\sqrt{2}}{1/\sqrt{2}}{0}{0}.

$$ The answer can only be blue or orange. We find the following retrieved contexts: $$\boldsymbol{x}_{\textsc{ Blue}}= \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \\0
\end{bmatrix}, \quad
\boldsymbol{x}_{\textsc{ Orange}}= \begin{bmatrix} 0 \\ 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} 
\end{bmatrix}.$$ Now, orange and blue are equally good matches for the cue 'Number': $$\begin{array}{ccc}
 \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Blue}}& = &
 \boldsymbol{x}_{\textsc{ Number}}\cdot \boldsymbol{x}_{\textsc{ Orange}}.
 \end{array}$$

In general, suppose we replace $k$ blue words in the blue treatment with $k$ orange words. Using numbers from the experiment: $$
\boldsymbol{x}_{\textsc{ Blue}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P_b(\textsc{ Blue},\textsc{ Number})}{\sqrt{P_b(\textsc{ Blue})P_b(\textsc{ Number})}} =
 \frac{15}{\sqrt{15+25 - k}\sqrt{15+10}}
$$ and $$\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P_b(\textsc{ Orange},\textsc{ Number})}{\sqrt{P_b(\textsc{ Orange})P_b(\textsc{ Number})}} =
 \frac{10}{\sqrt{10 + k}\sqrt{15+10}}$$ At around $k = 5.4$, the model no longer predicts that participants will recall that orange is more likely.

We next show how the model addresses results in (Kahneman and Tversky 1973), and in particular, Example 1. In this case, we do not know subjects' database (other than the base rates), which was an advantage we had in modeling the (Bordalo et al. 2021) experimental framework.

Recall that the first group of subjects is not given the description of Tom W., and is asked to report the base rates of the 9 fields of study (Kahneman and Tversky 1973, Table 2). This table gives a base rate for the humanities, for example, as 20%, and for computer science as 7%. The second and third groups are given the description and asked to rank the likelihood that Tom W. majors in a subject and the "similarity" (the words of Kahneman and Tversky (1973)) between Tom W. and the subject, respectively. For the moment, we ignore the similarity rank and focus on what Kahneman and Tversky (1973) term the likelihood rank of a major, which corresponds to the Bayesian posterior. The Bayesian calculation implies $$
P(\textsc{ Field}| \textsc{ Tom}) \propto P(\textsc{ Tom}|\textsc{ Field})\underbrace{P(\textsc{ Field})}_{\text{base rate}}, 
\quad \textsc{ Field}\in\{\textsc{ Computers},\textsc{ Humanities}\}.

$$ If there were zero humanities majors that resembled Tom W. in subjects' database then ranking the probability that Tom W. is a computer scientist higher than a humanities major is consistent with Bayesian reasoning. This is clearly not what Kahneman and Tversky (1973) have in mind, and they argue against this possibility. Nevertheless, without knowledge of the subjects' database, it is not possible to rule this scenario out. In this case, both the Bayesian model and our model would produce the observed result.

However, there is a wide range of probabilities under which our model would produce a different result than the Bayesian model. This range consists of cases that broadly resemble Study 1 of (Bordalo et al. 2021), namely instances of Tom W. appear more frequently among humanities majors than computer science majors, but that they are difficult to recall because there are many other types of people majoring in the humanities. Table  maps the Tom W. experiment into the words/numbers experiment.

 ----------------- -- ------------------------------------------------------------------- -- ----------------------------- -- ----------------------- -- --
 Role in Theorem 1 Kahneman and Tversky (1973) Bordalo et al. (2021) 
 cognitive model notation experiment experiment 
 Cue $d$ Tom W. Number 
 Decoy $-d$ Other people Word 
 Target 1 $h$ Computer science Orange 
 Target 2 $-h$ Humanities Blue 
 ----------------- -- ------------------------------------------------------------------- -- ----------------------------- -- ----------------------- -- --

 : Mapping between cognitive model and experimental settings

Specifically, consider Tom W. to be the cue and the targets to be the various fields of study (majors). As an illustration of where our model would make a different prediction than Bayesian inference, consider the case in which there are 7 computer science majors for every 20 humanities majors, therefore matching the proportions in base rates. Assume all computer science majors resemble Tom W., but half of the humanities majors do so. In this case, memory databases will be such that $$\begin{eqnarray*}
\boldsymbol{x}_{\textsc{ Computers}}\cdot \boldsymbol{x}_{\textsc{ Tom}}& \propto &
 \frac{P(\textsc{ Computers},\textsc{ Tom})}{\sqrt{P(\textsc{ Computers})}}
 = \frac{7}{\sqrt{7}}\\
\boldsymbol{x}_{\textsc{ Humanities}}\cdot \boldsymbol{x}_{\textsc{ Tom}}& \propto &
 \frac{P(\textsc{ Humanities},\textsc{ Tom})}{\sqrt{P(\textsc{ Humanities})}}
 = \frac{10}{\sqrt{20}}
\end{eqnarray*}$$ and thus, $\boldsymbol{x}_{\textsc{ Computers}}\cdot \boldsymbol{x}_{\textsc{ Tom}}>\boldsymbol{x}_{\textsc{ Humanities}}\cdot \boldsymbol{x}_{\textsc{ Tom}}$. Assuming (as (Kahneman and Tversky 1973) implicitly do) that the memory databases on average are the same among the third group that assess likelihoods as the first group that assesses base rates, this would explain why computer science is judged as a more likely major for Tom W. than is the humanities. Note that Bayesian inference leads to the opposite conclusion in this case: $$\begin{eqnarray*}
P(\textsc{ Computers}\cond \textsc{ Tom}) & \propto & P(\textsc{ Tom}\cond\textsc{ Computers})P(\textsc{ Computers}) = P(\textsc{ Tom},\textsc{ Computers}) = 7/27 \\
 P(\textsc{ Humanities}\cond\textsc{ Tom}) & \propto & P(\textsc{ Tom}\cond\textsc{ Humanities})P(\textsc{ Humanities}) = P(\textsc{ Tom},\textsc{ Humanities}) = 10/27
\end{eqnarray*}$$ Thus the model accounts for the Tom W. experiment in (Kahneman and Tversky 1973).

Finally, recall that there is a second group that assesses similarities. While the analysis above does not require that we take a stance on what (Kahneman and Tversky 1973) mean by "similarity," their use of the word is consistent with the general idea that it is contextual similarity that drives probabilistic judgement.

## Quantitative results 

The model above is stylized. It abstracts, for example, from initial associations $M_0$. It also abstracts from contextual dynamics, employing a minimalist version of autoregressive context. Finally, the temporal context model does not itself explain all aspects of memory. All of these are potential sources of errors in the model. We encapsulate these sources of error in a simple way by assuming that inner products are perceived with noise by the agent. Assuming perception occurs with noise is standard (Stanislaw and Todorov 1999), see also (Kahana 2012, chap. 2). The addition of a single parameter allows the model to quantitatively fit the data of (Bordalo et al. 2021).

In this extension, the criterion for stating orange is more likely is $$(\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{Number}})e^{\tilde{\epsilon}_{\textsc{Orange}}} > \left(\boldsymbol{x}_{\textsc{Blue}}\cdot\boldsymbol{x}_{\textsc{Number}}\right)e^{\tilde{\epsilon}_{\textsc{Blue}}},$$ where $\tilde{\epsilon}$ are agent-specific random variables.[^12] Substituting into the solution and expressing in terms of the error terms, this threshold is equivalently $$\frac{P_b(\textsc{ Orange},\textsc{ Number})}{P_b(\textsc{ Blue},\textsc{ Number})}\sqrt{\frac{P_b(\textsc{ Blue})}{P_b(\textsc{ Orange})}} > e^{\tilde{\epsilon}_{\textsc{Blue}} -\tilde{\epsilon}_{\textsc{Orange}}}.$$ Taking the log and substituting in the values from (Bordalo et al. 2021), we find that a participant in the gray treatment states that $$\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{15}{10}\right) \approx -0.20 > \tilde{\epsilon}_{\textsc{Blue}} -\tilde{\epsilon}_{\textsc{Orange}},$$ and a participant in the blue treatment will say that orange is more likely if $$\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{40}{10}\right) \approx 0.29 > \tilde{\epsilon}_{\textsc{Blue}} -\tilde{\epsilon}_{\textsc{Orange}}.$$ The latter criterion is more likely to be met, so those in the blue condition will tend to respond orange at a higher rate.

Suppose now that $\tilde{\epsilon}_{\textsc{Blue}}$ and $\tilde{\epsilon}_{\textsc{Orange}}$ are iid normally distributed. In this case, their difference $$\tilde{\epsilon} \equiv \tilde{\epsilon}_{\textsc{Blue}} -\tilde{\epsilon}_{\textsc{Orange}} \sim N(0,\sigma^2)$$ for some variance $\sigma^2$. Under this assumption, the proportion of participants who judge orange numbers to be more likely than blue numbers will simply be given by the normal CDF. Let $\Phi(z)$ denote the standard normal CDF. The proportion in the gray treatment equals $$\Phi\left(\frac{1}{\sigma}\left(\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{15}{10}\right)\right)\right),$$ and the proportion in the blue treatment will equal $$\Phi\left(\frac{1}{\sigma}\left(\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{40}{10}\right)\right)\right).$$ The latter is larger than the former, as found in the experiment.

For Study 2, we want to know how the answer changes if we replace the $k$ blue words in the blue treatment with the $k$ orange words. In this case, the participant will say that orange is more likely if $$\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{40-k}{10+k}\right) > \tilde{\epsilon},$$ which is less likely to be true for high values of $k$. The proportion of participants is then $$\Phi\left(\frac{1}{\sigma}\left(\log\left(\frac{10}{15}\right) + \frac{1}{2}\log\left(\frac{40-k}{10+k}\right)\right)\right),$$ which falls in $k$, matching the experimental results.

### Model fit

To fit the model to the data of (Bordalo et al. 2021), we estimate $\sigma$ by minimizing the distance between all moments in the data and model, where the data come from Figures 1 and 2 of (Bordalo et al. 2021).[^13] Specifically, we estimate $\sigma$ to be $$\hat{\sigma} = \underset{\sigma}{\text{argmin}} \biggl\{\text{error}(\sigma)^\top\text{error}(\sigma)\biggr\},$$ where $\text{error}(\sigma)$ is a vector of (percent) errors with $j$th element $$\text{error}_j(\sigma) = \frac{\textrm{data moment}_j - \textrm{model moment}_j(\sigma)}{\textrm{data moment}_j}.$$ This procedure gives an estimate of $$\hat{\sigma} \approx 1.3737.$$ Figures 2 and 3 plot the resulting moments, and show that the model provides an excellent fit across the experimental conditions.

<figure id="fig:BCGSS_fig1_est" data-latex-placement="p">
<embed src="../Code/plots/BCGSS_1_est.pdf" style="width:50.0%" />
<figcaption>Study 1, Figure 1 of <span class="citation" data-cites="Bordetal:21Rep">(Bordalo et al. 2021)</span>. The noise parameter <span class="math inline"><em>σ</em></span> is estimated to match all moments in Figures <a href="#fig:BCGSS_fig1_est" data-reference-type="ref" data-reference="fig:BCGSS_fig1_est">2</a> and <a href="#fig:BCGSS_fig2_est" data-reference-type="ref" data-reference="fig:BCGSS_fig2_est">3</a>.</figcaption>
</figure>

<figure id="fig:BCGSS_fig2_est" data-latex-placement="p">
<figure>
<embed src="../Code/plots/BCGSS_2a_est.pdf" />
<figcaption><span class="citation" data-cites="Bordetal:21Rep">Bordalo et al. (2021)</span> Figure 2a</figcaption>
</figure>
<figure>
<embed src="../Code/plots/BCGSS_2b_est.pdf" />
<figcaption><span class="citation" data-cites="Bordetal:21Rep">Bordalo et al. (2021)</span> Figure 2b</figcaption>
</figure>
<figcaption>Study 2, Figure 2 of <span class="citation" data-cites="Bordetal:21Rep">(Bordalo et al. 2021)</span>. The noise parameter <span class="math inline"><em>σ</em></span> is estimated to match all moments in Figures <a href="#fig:BCGSS_fig1_est" data-reference-type="ref" data-reference="fig:BCGSS_fig1_est">2</a> and <a href="#fig:BCGSS_fig2_est" data-reference-type="ref" data-reference="fig:BCGSS_fig2_est">3</a>.</figcaption>
</figure>

## Comparison with a probabilistic model 

The previous sections, together with Appendices 7 and 8, show that the model can account for the evidence in (Bordalo et al. 2021). Here, we compare our model to theirs.

Building on (Gennaioli and Shleifer 2010) and (Bordalo et al. 2016), (Bordalo et al. 2021) specify a reduced-form model with the ability to capture deviations from Bayesian updating. They define a similarity function $S(d,h)$, to which they apply a Luce choice rule (see Appendix 7) to determine the subjective probability: $$
\Pti(h|d) = \frac{e^{S(d,h)}}{e^{S(d,h)} + e^{S(d,\neg h)}},

$$ where $$
S(d,h) = \alpha f(P(d,h)) - \gamma f(P(-d,h)),

$$ and where $f$ is an increasing function, parameterized by $f(x) =
\log (c +x)$ for a constant $c$. Under this parameterization, the model captures Bayesian inference when $\alpha = 1$ and $\gamma = c =
0$. Note that in this model, by construction, the likelihood assessments increase in $P(h|d)$ (which is necessary for basic plausibility) and decrease in $P(h|{-d})$ (without which the model would ultimately resemble a Bayesian one). As described above, these are also key implications of our cognitive theory.

An important difference between the models is that, in the (Bordalo et al. 2021) model, $\gamma$ is a flexible parameter, introduced to fit the representativeness heuristic. In contrast, our model provides a cognitive foundation for $\gamma$, and in so doing eliminates $\gamma$ entirely as a free parameter.[^14] A second key difference is that the Bordalo et al. (2021) model is fundamentally based on probability distortion, whereas our model is based on recognition memory. To illustrate the benefits of a cognitive framework, we turn to the conjunction fallacy.

# The conjunction fallacy 

In the previous section, the possible targets were mutually exclusive: for example, a number could be either blue or orange, but not both. We now relax that assumption, and in the process address a second puzzle, the conjunction fallacy. (Tversky and Kahneman 1983) present a wide range of experimental findings in which subjects judge a conjunction of two statements to be significantly more likely than one of the constituent statements, a violation of the laws of probability. We describe one of their experiments in detail.

**Example 3** ((Tversky and Kahneman 1983)). *Subjects are given a description of an outspoken, single woman who is passionate about social-justice issues. They report that it is less likely that she is a bank teller than that she is both a bank teller and a feminist, even though this is logically impossible. Similarly, when given a description of a mathematical but unimaginative man, subjects report that it is less likely that he is a jazz player than that he is an accountant and a jazz player.*

 Possibilities for Linda Possibilities for Bill
 ------------------------------------------------------ --------------------------------------------------
 Linda is a teacher in elementary school. Bill is a physician who plays poker for a hobby.
 Linda works in a bookstore and takes Yoga classes. Bill is an architect.
 Linda is active in the feminist movement. (F) Bill is an accountant. (A)
 Linda is a psychiatric social worker. Bill plays jazz for a hobby. (J)
 Linda is a member of the League of Women Voters. Bill surfs for a hobby.
 Linda is a bank teller. (T) Bill is a reporter.
 Linda is an insurance salesperson. Bill is an accountant who plays jazz for a
 Linda is a bank teller and is active in the feminist hobby. (A&J)
 movement. (T&F) Bill climbs mountains for a hobby.

 : This table lists the possibilities given to participants in the conjunction experiment of (Tversky and Kahneman 1983). See the main text for details about the experiment.

\

In this experiment, participants read a description of a woman named Linda and a man named Bill. About Linda, they read: "Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations." About Bill, they read: "Bill is 34 years old. He is intelligent, but unimaginative, compulsive, and generally lifeless. In school, he was strong in mathematics but weak in social studies and humanities." Subjects were then asked to rank, in order of likelihood, the possibilities given in Table 2. Over 80% of participants rank, from more to less likely, F$>$T&F$>$T for Linda and A$>$A&J$>$J for Bill. Regardless of beliefs, this likelihood ranking is a logical impossibility. (Tversky and Kahneman 1983) refer to the tendency of subjects to rank the conjunction as more likely than one of the constituents as the *conjunction fallacy*.

Here, we show how the model explains this fallacy. We first give an example and then a formal proof. Consider subjects asked to rank the probability that Bill is an accountant (A), a jazz player (J), or both (A $\cap$ J) (see Table 2). While Bill as presented in the (Tversky and Kahneman 1983) experiment may be a composite representation, we simplify notation by representing Bill as basis vector $f_{\textsc{ Bill}}$. The features space in this simplified example is: $$\begin{array}{ccc}
\sc Bill& \sc Accountant (A)& \sc Jazz player (J) \\
\updownarrow & \updownarrow & \updownarrow \\
\myvectoriii{1}{0}{0}& \myvectoriii{0}{1}{0}& \myvectoriii{0}{0}{1}
\end{array}$$ Assume Bill is seen in a context that makes it clear that he is an accountant. Subjects see jazz players, and they also see accountants who are not Bill. Thus: $$
\begin{array}{ccccc}
 Bill as Accountant & // & Accountant& // & Jazz Player \\
 \underbrace{\myvectoriii{1}{0}{0},\myvectoriii{0}{1}{0}} & & \myvectoriii{0}{1}{0}& &
 \myvectoriii{0}{0}{1}\\
 \boldsymbol{x}_1 & & \boldsymbol{x}_2 & & \boldsymbol{x}_3\\
 \myvectoriii{1}{0}{0}& &\myvectoriii{0}{1}{0}& & \myvectoriii{0}{0}{1}
\end{array}

$$ The mental representation ) implies that the memory matrix is equal to: $$M = M_0 + \myvectoriii{1}{0}{0}\!\begin{array}{c}[\,1 \ \ 1 
 \ \ 0 \,]\\ ~ \\
 ~\end{array} + \myvectoriii{0}{1}{0}\!\begin{array}{c}[\,0 \ \ 1 
 \ \ 0 \,]\\ ~ \\
 ~\end{array} + \myvectoriii{0}{0}{1}\!\begin{array}{c}[\,0 \ \ 0 
 \ \ 1 \,]\\ ~ \\
 ~\end{array},$$ With $M_0$ equal to the zero matrix, $$M = \begin{bmatrix}
 1 & 1 & 0 \\
 0 & 1 & 0\\
 0 & 0 & 1
 \end{bmatrix}$$ In the experiment, the cue is the feature 'Bill': $$\boldsymbol{x}_{\textsc{ Bill}}\equiv \frac{M f_{\textsc{ Bill}}}{\norm{Mf_{\textsc{ Bill}}}} \propto \myvectoriii{1}{0}{0},$$ which picks up the single context in which Bill is seen.

The targets are Accountant together with Jazz, Accountant, and Jazz: $$\begin{eqnarray}
\boldsymbol{x}_{\textsc{
 A}\cap\textsc{ J}}& \equiv & \frac{M(f_{\textsc{ A}}+ f_{\textsc{ J}}) }{\norm{M(f_{\textsc{ A}}+ f_{\textsc{ J}}) }} =
 \begin{bmatrix} 1/\sqrt{3} \\ 1/\sqrt{3} \\ 1/\sqrt{3}\end{bmatrix}\\
\boldsymbol{x}_{\textsc{ J}}& \equiv & \frac{Mf_{\textsc{ J}}}{\norm{Mf_{\textsc{ J}}} } = \myvectoriii{0}{0}{1}\\ 
\boldsymbol{x}_{\textsc{ A}}& \equiv & \frac{Mf_{\textsc{ A}}}{\norm{Mf_{\textsc{ A}}}} = \begin{bmatrix}
 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{bmatrix}
\end{eqnarray}$$ From which we see that $$\boldsymbol{x}_{\textsc{ Bill}}\cdot \boldsymbol{x}_{\textsc{ A}}> \boldsymbol{x}_{\textsc{ Bill}}\cdot \boldsymbol{x}_{\textsc{
 A}\cap\textsc{ J}}> \boldsymbol{x}_{\textsc{ Bill}}\cdot \boldsymbol{x}_{\textsc{ J}}.$$ Rather than assessing probabilities through traditional inference (which would lead, through the laws of probability, to the chance of Accountant and Jazz player being less than or equal to Jazz player), participants assess probabilities through context matches with a target. Because Accountant and Jazz player contains within it the word "Accountant," this composite feature brings up the context associated with Accountant. While not as good a match as Accountant on its own, it is still better than Jazz on its own.

To generalize from this specific example, we translate the problem into the formal language of Section 3. Recall that $\Omega = \calH\times \calD$. Implicit in this definition is that members of the population are identified by a single hypothesis and a single cue. We now allow members to be potentially identified by two hypotheses, one in the set $\calH_1$, and one in the set $\calH_2$, so that $\Omega = \calH_1\times\calH_2\times\calD$. Note that any probability measure $P$ over $\Omega$ is also a probability measure over $\calH_1$ and $\calH_2$. Thus, $P(h_{1,j}) =
\sum_{h_{2,k}\in \calH_2} P(h_{1,j},h_{2,k})$, for $h_{1,j}\in\calH_1$. Clearly $P(h_{1,j},h_{2,k})\leq P(h_{1,j})$, with a strict inequality provided that $P$ allows some instances of $h_{1,j}$ to occur with an element of $\calH_2$ other than $h_{2,k}$.

In this example, it is useful to allow agents to view elements that are in $\calH_1\times\calH_2\times\calD$, in $\calH_1\times \calD$, in $\calH_2\times\calD$, or only in $\calH_1$ and $\calH_2$. Because all elements of $\Omega$ have attributes in each of these sets, we need to extend our definitions to allow the agent to view certain subsets $\Omega$. For example, if an agent observes someone to be an accountant but does not know if the person also plays jazz, then the agent is observing a subset of $\Omega$ rather than a specific element. If it becomes known whether the individual is a jazz player or not, the subset resolves into a single element. We let $\wp(\Omega)$ denote this broader set of admissible subsets.

We maintain the assumption of Section 3 that $f_{h_{1, j}}$ and $f_{h_{2,j}}$, etc., are basis vectors. The following naturally extends to the model of Section 3 to account for the conjunction fallacy.

**Model Summary 2** (Conjunctions). *Suppose that an agent views the $n$ elements of $\wp(\Omega)$ as feature vectors $f_i,$ $i = 1,\ldots, n$. If $f_i = f_{h_1}, f_{h_2}, f_d$, for $h_j \in \calH_j$, $f_d\in\calD$, then $f_i$ is a basis vector; otherwise $f_i$ is a composite representation. Feature vectors $f_i$ combine with orthogonal contexts $\boldsymbol{x}_i$ to form memory $M$ as in ), with $M_0$ the zero matrix. Let $f_\mathcal{j},$ $\mathcal{j}\in \calH_1\cup
\calH_2 \cup (\calH_1\times\calH_2) \cup \calD$ represent a cue ($d\in \calD$), a target ($h_1\in \calH_1, h_2\in\calH_2$), or a conjunction target ($h_1\cap h_2\in\calH_1\times\calH_2$). In the case of the conjunction target, the agent forms the composite representation. When cued with $d$, the agent ranks the conjunction target $h_1\cap h_2$ as more likely than $h_1$ (given cue $d$) if $$
\boldsymbol{x}_d\cdot \boldsymbol{x}_{h_1\cap h_2} > \boldsymbol{x}_d \cdot \boldsymbol{x}_{h_1},

$$ where $\boldsymbol{x}_\mathcal{j}$ is a norm-1 retrieved context vector such that $\boldsymbol{x}_{\mathcal{j}} \propto M
f_{\mathcal{j}}$.[^15]*

In this setting, the conjunction fallacy arises under the following conditions.

**Theorem 5**. *Suppose that the agent's sample matches the population in that items appear in their correct proportions. Then $$\begin{eqnarray}
\boldsymbol{x}_d\cdot \boldsymbol{x}_{h_1\cap h_2} & = & 
\frac{P(h_1,d)+P(h_2,d)}{\sqrt{(P(h_1)+P(h_2)+2P(h_1\cap h_2)) P(d)}} \\
\boldsymbol{x}_d\cdot \boldsymbol{x}_{h_1} & = & \frac{P(h_1,d)}{\sqrt{P(h_1)P(d)}}. 
\end{eqnarray}$$ Moreover, ) is equivalent to: $$
1 + \frac{P(h_2|d)}{P(h_1|d)} >
\sqrt{1+\frac{P(h_2)}{P(h_1)}+2P(h_1|h_2)}.

$$*

*Proof.* Equation  follows from the 2, with the composite representation $f_{h_1} + f_{h_2}$ forming the cue. Equation  follows from Theorem 1. Given ), ) follows from substituting ) and ) into ), dividing both sides by $\sqrt{P(d)}$ to create conditional probabilities and then rearranging, noting that, by the laws of probabilities, $P(h_1\cap h_2)/P(h_2) = P(h_1\cond h_2)$.

Therefore, it suffices to prove ). Consider that $$\boldsymbol{x}_{h_1\cap h_2} \propto M(f_{h_1} + f_{h_2})$$ The unscaled context vector $M(f_{h_1} + f_{h_2})$ will have entries equal to 1 corresponding to times when either $h_1$ or $h_2$ are observed (but not both) and a 2 corresponding to times when both $h_1$ and $h_2$ are observed. Therefore, $(M(f_{h_1} +
f_{h_2}))^\top M(f_{h_1} +
f_{h_2}) = \#\{h_1\cap (-h_2) \} + \#\{h_2\cap (-h_1)\} + 4\#\{h_1\cap
h_2\} = \#\{h_1\} + \#\{h_2\} + 2\#\{h_1\cap h_2\}$. When divided by the total number of elements in the population, this becomes $P(h_1)+P(h_2)+2P(h_1\cap h_2)$. In the numerator, we see cases where $d$ and $h_1$ coincide, and $d$ and $h_2$ coincide. There are $\#\{h_1\cap d\} + \#\{h_2 \cap d\}$ cases. Dividing by the number of elements in the population yields ). ◻

Suppose, for instance, that there are no observations of Bill as a jazz player. The assessed probability that Bill could be both a Jazz player and an accountant is still greater than zero, though less than an accountant alone.

This application highlights the role of the cognitive model in that one would not obtain these results by applying the probability rule ) to the conjunction. To consider a simple example, suppose that someone like Bill was never observed to be a jazz player. According to ), the subject would rank the probability as zero. In contrast, the model above allows the cue jazz and accountant to work together, so that relevant instances are still brought to mind.

# Associative recognition in financial markets 

The recognition mechanism has broad implications for financial markets. In this section, we develop a series of applications in which associative recognition---the retrieval of different contexts by different cues---leads to systematic departures from rational pricing. Each application shares a common structure: a cue $d$ retrieves a context $\boldsymbol{x}_d$ that determines how investors assess the probability of a financial outcome. When cues that are economically equivalent retrieve dissimilar contexts, prices diverge from fundamentals.

## Negative stub values 

(Lamont and Thaler 2003) document cases in which a parent company is valued by the market at less than the value of its ownership stake in a publicly traded subsidiary, implying that the parent's remaining assets have negative value. The most prominent case involves 3Com and Palm. On March 2, 2000, 3Com sold a fraction of its stake in Palm via an IPO. 3Com retained ownership of 95% of Palm's shares and announced its intention to spin off the remaining shares to 3Com shareholders. After the first day of trading, Palm closed at \$95.06 per share, implying that the price of 3Com should have been at least \$145 (given 3Com shareholders' claim on 1.5 Palm shares each). Instead, 3Com fell to \$81.81. The "stub value" of 3Com---the implied value of its non-Palm assets---was $-\$63$.

Why does this violate the law of one price so dramatically? (Lamont and Thaler 2003) identify short-sale constraints as the proximate friction, but note that frictions alone cannot explain why investors willingly pay more to own Palm directly than to own Palm embedded in 3Com. The demand side requires "irrational" investors. Our model provides a specific cognitive mechanism.

In the framework of Theorem 1, the cues are the company names themselves: "Palm" ($d_{\textsc{ Palm}}$) and "3Com" ($d_{\textsc{ 3Com}}$). The hypotheses are whether the company is a new-economy stock ($h$) or an old-economy stock ($-h$). In March 2000, new-economy stocks had recently experienced extraordinary returns, so being classified as new-economy is associated with high expected returns.

The name "Palm" retrieves a context vector $\boldsymbol{x}_{d_{\textsc{ Palm}}}$ rich in new-economy, high-growth technology associations. The name "3Com" retrieves a different context vector $\boldsymbol{x}_{d_{\textsc{ 3Com}}}$ laden with legacy-networking, old-economy associations. Even though Palm's payoffs are mechanically a subset of 3Com's, the two names evoke different contexts, and investors judge $$\boldsymbol{x}_{d_{\textsc{ Palm}}}\cdot\boldsymbol{x}_h \;>\;
\boldsymbol{x}_{d_{\textsc{ 3Com}}}\cdot\boldsymbol{x}_h.$$ The market effectively prices the two companies as if they inhabit different probability spaces. Investors bid up Palm because its name retrieves a context in which firms like Palm have done well, while 3Com's name does not---despite the fact that owning 3Com is economically superior to owning Palm alone.

This prediction is unique to our framework. In models based on probability distortion, such as diagnostic expectations (Bordalo et al. 2018), the distorted probability preserves the algebra of probability: if Palm's payoffs are a subset of 3Com's, then $\hat{P}(\text{Palm does well} | d) \leq \hat{P}(\text{3Com does well} | d)$. In recall-based models, sampling from memory and counting successes mechanically ensures that a subset cannot outrank the whole. Our model breaks this logic because Palm and 3Com are evaluated via different cues that retrieve different contexts. The prediction of negative stubs is thus a qualitative test that separates the recognition mechanism from all existing alternatives.[^16]

## Name changes 

The recognition mechanism predicts that changes to the cue---even those carrying no new information about fundamentals---will shift investor beliefs if they alter the retrieved context. A striking example is the effect of corporate name changes during the dot-com era. (Cooper et al. 2001) document that firms adding ".com" or "Internet" to their names experienced cumulative abnormal returns of approximately 74% in the ten days surrounding the announcement, regardless of the extent of their actual Internet involvement. When the bubble burst, firms that dropped Internet-related names saw positive abnormal returns.

In our framework, the company name is a component of the cue $d$. Appending ".com" transforms $d$ into $d'$, which retrieves a context vector $\boldsymbol{x}_{d'}$ laden with high-growth technology associations---even if the firm's operations are unchanged. The retrieved context has higher cosine similarity with the "high returns" target $\boldsymbol{x}_h$, so investors judge the firm more likely to be a high-growth company: $$\boldsymbol{x}_{d'}\cdot\boldsymbol{x}_h > \boldsymbol{x}_d\cdot\boldsymbol{x}_h.$$ No new information has arrived. The name change simply alters which past experiences the cue brings to mind. This is a pure recognition effect: the investor's flash of recognition---does this firm "go with" high returns?---is governed by the context the cue retrieves, and a name carrying Internet connotations retrieves a fundamentally different context than a traditional industrial name. Dropping the Internet-related name reverses the effect, as the cue $d$ reverts to retrieving its original context.

## Stock splits and reverse splits 

A stock split changes the nominal share price without altering the firm's market capitalization, cash flows, or any other fundamental. Yet splits are associated with substantial abnormal returns. (Ikenberry et al. 1996) find one-year abnormal returns of approximately 8% following two-for-one splits, and (Desai and Jain 1997) find one-year abnormal returns of approximately $-11$% following reverse splits, with three-year returns of $-34$%.

Our model identifies two distinct recognition channels through which a split affects investor beliefs. The first operates through the split event itself. Firms that split their stock tend to be high-quality, high-growth firms whose managers are confident about future performance (Ikenberry et al. 1996). This creates an association in the memory matrix $M$: the feature "this firm split its stock" is encoded in contexts associated with subsequent high returns. When a new split is announced, the cue $d_{\mathrm{split}}$ retrieves these contexts, and investors judge the firm more likely to be a high-quality investment. The second channel operates through the nominal price level. (Birru and Wang 2016) document a "nominal price illusion": investor expectations of upside potential jump discontinuously on the split date, even though actual future skewness decreases. In our framework, the lower post-split price retrieves contexts associated with high-growth firms (which tend to have low share prices), reinforcing the first channel. (Baker et al. 2009) provide complementary evidence that firms actively manage their nominal share price to cater to time-varying investor preferences for certain price ranges.

Reverse splits provide further evidence for the event-association channel. Firms that reverse-split are overwhelmingly distressed firms trying to avoid delisting. The cue $d_{\mathrm{reverse}}$ therefore retrieves contexts laden with associations of financial distress, and the strongly negative abnormal returns ($-11$% at one year, $-34$% at three years) confirm this prediction.[^17] Letting $h$ denote the hypothesis of high future returns, $$\boldsymbol{x}_{d_{\mathrm{split}}}\cdot\boldsymbol{x}_h \;>\;
\boldsymbol{x}_{d}\cdot\boldsymbol{x}_h \;>\;
\boldsymbol{x}_{d_{\mathrm{reverse}}}\cdot\boldsymbol{x}_h,$$ where $d$ denotes the cue without the split event. Both forward and reverse splits illustrate the same principle: the event creates an association in memory, and that association shifts beliefs about future returns through the recognition channel.

## Mental accounts for prices and dividends 

(Hartzmark and Solomon 2019) document that investors treat stock price changes and dividends as disconnected attributes rather than combining them into total returns as standard finance theory predicts. Individual investors, mutual funds, and institutions are all less likely to sell dividend-paying stocks; the disposition effect---the tendency to sell winners and hold losers---tracks price changes rather than total returns; analysts' price forecasts neglect the mechanical price decline on ex-dividend dates; and dividend reinvestment is rare even among institutional investors. Hartzmark and Solomon (2019) term the resulting error the "free dividends fallacy": because investors do not perceive the tradeoff between dividends and price declines, dividends appear to be a costless source of income.

Associative recognition provides a cognitive foundation for this disconnect. In our framework, the relevant cue is the stock's recent performance. However, a stock's performance has two attributes: the price change $\Delta p$ and the dividend payment $\delta$. When these attributes are encoded in separate contexts (because they are experienced at different times or through different information channels), they retrieve dissimilar context vectors, just as Palm and 3Com retrieve different contexts despite being economically linked.

Formally, let $d_{\Delta p}$ denote the cue associated with the price change and $d_\delta$ the cue associated with the dividend payment. When the investor assesses whether the stock is performing well (target $h$), each cue retrieves its own context: $\boldsymbol{x}_{d_{\Delta p}}$ and $\boldsymbol{x}_{d_\delta}$. Because dividends are experienced as small, stable, positive payments while price changes are experienced as large, volatile movements, these cues retrieve different contexts: $$\boldsymbol{x}_{d_\delta}\cdot\boldsymbol{x}_h \neq
\boldsymbol{x}_{d_{\Delta p}}\cdot\boldsymbol{x}_h.$$ The investor evaluates the two attributes separately rather than combining them into a single return $r = \Delta p/p + \delta/p$. Dividends, encoded in a context of stability and positive income, consistently retrieve a context similar to the "good outcome" target. This generates the free dividends fallacy: the investor judges dividend-paying stocks favorably on the dividend dimension while separately (and independently) evaluating them on the price-change dimension. The result is a failure of the arbitrage mechanism embedded in Miller--Modigliani irrelevance, as investors who mentally account for price and dividend returns separately will pay a premium for dividend-paying stocks when the appeal of stable income is high---precisely the pattern Hartzmark and Solomon (2019) document.

## The cross-section of stock returns and excess volatility 

The recognition mechanism also speaks to two long-standing quantitative puzzles in finance: the value premium and excess volatility.

#### The cross-section of stock returns.

Growth stocks---those with low book-to-market ratios---earn lower average returns than value stocks, a pattern difficult to attribute to conventional risk (Fama and French 1992; Lettau and Wachter 2007). (La Porta 1996) documents that stocks with high analyst long-term growth (LTG) forecasts subsequently underperform, a result replicated by (Bordalo et al. 2019a); (Guo and Wachter 2025) connect this bias explicitly to the value premium, showing that growth companies receive upward-biased forecasts relative to value companies.

Let $\Omega$ denote the population of firms. Each firm $i\in\Omega$ has an expected annual growth rate of earnings $\lambda_i\in\{\lambda_\ell,\lambda_\calh\}$, where $\lambda_\ell<\lambda_\calh$. Let $G_{iT}$ denote average past growth for firm $i$, categorized as either high ($G_{iT}\in\mathcal{G}_\calh\equiv d$) or low ($G_{iT}\in\mathcal{G}_\ell\equiv {-d}$). Analysts observe each firm and encode the pair $\{G_{iT},\lambda_i\}$ in the same context, forming the memory matrix $M$.[^18] We are in the setting of Theorem 1. The cue is past growth $\calG_\calh$; the targets are $\lambda_\calh$ and $\lambda_\ell$. The agent judges a high-past-growth firm to be high-growth if $$\boldsymbol{x}_{\lambda_\calh}\cdot\boldsymbol{x}_{\calG_\calh} = \frac{P(\lambda_\calh,G\in\mathcal{G}_\calh)}{\sqrt{P(\lambda_\calh)}}
> \frac{P(\lambda_\ell,G\in\mathcal{G}_\calh)}{\sqrt{P(\lambda_\ell)}} = \boldsymbol{x}_{\lambda_\ell}\cdot\boldsymbol{x}_{\calG_\calh},$$ which is more likely when high-growth firms are rare. Table 3 maps the variables. The mechanism is the same as in the experimental setting: the abundance of low-past-growth firms with $\lam_\ell$ erodes the retrieval strength of the decoy association ($\calG_\calh$, $\lam_\ell$). Investors bid up the prices of firms they judge as high-growth; as more data arrives and $P(\lam_\calh|\calG_\calh)\to 0$ or $1$ (Theorem 3), errors correct and returns disappoint---generating the value premium.

 ----------------- -- ------------------------------------------------------------------- -- ----------------------- -- --------------------------------- -- --------------------------------------- -- --
 Role in Theorem 1 Bordalo et al. (2021) Earnings Recession 
 cognitive model notation experiment expectation Forecasting 
 Cue $d$ Number High past growth $\calG_\calh$ Recession indicators $\calG_\calr$ 
 Decoy $-d$ Word Low past growth $\calG_\ell$ Normal-times indicators $\calG_\caln$ 
 Target 1 $h$ Orange High future growth $\lam_\calh$ Recession $z_{t+1}=1$ 
 Target 2 $-h$ Blue Low future growth $\lam_\ell$ Normal times $z_{t+1}=0$ 
 ----------------- -- ------------------------------------------------------------------- -- ----------------------- -- --------------------------------- -- --------------------------------------- -- --

 : Mapping between cognitive model and economic forecasts

#### Excess volatility.

Stock prices, investment, and unemployment all exhibit volatility that rational-expectations models struggle to match (Campbell and Shiller 1988; Gourio 2012; Hall 2017). Our framework offers a parsimonious explanation. Let $z_t\in\{0,1\}$ indicate a recession and let $\calG_t\in\{\calG_\calr,\calG_\caln\}$ summarize current economic indicators. As above, agents encode indicator--outcome pairs $(\calG_t,z_{t+1})$ in their memory matrix and judge the likelihood of a recession by comparing $\boldsymbol{x}_{\calG_t}\cdot\boldsymbol{x}_\calr$ with $\boldsymbol{x}_{\calG_t}\cdot\boldsymbol{x}_{\caln}$. Because growth is largely unpredictable, even mildly negative indicators evoke the recession context---agents overreact to signals that a Kalman filter would largely ignore.[^19] These exaggerated beliefs lower stock valuations and depress hiring and capital expenditures; when the recession fails to materialize, valuations rebound on surprisingly good news---generating the excess volatility observed in the data.

# Conclusion 

This paper provides a cognitive foundation for Kahneman and Tversky's representativeness heuristic based on associate principles of memory. Our key insight is that, while apparently probabilistic in nature, the questions posed by the Kahneman and Tversky experiments are in fact about similarity. Thus, they are amenable to the tools of associative memory and, in particular, of retrieved context. Whether or not items are experienced under the same context governs whether the agent or subject views such items as similar, and ultimately drives likelihood judgements.

The associative memory approach leads to a theory of inference that is highly non-Bayesian but also tightly disciplined by both theory and experimental observation. We build on the foundational work of (Bordalo et al. 2021) to show that our model can not only explain the qualitative and narrative-based Kahneman and Tversky results, but also provide a quantitative fit to the experimental results obtained in a controlled setting. We build on a previous model of the paired associates (specifically associative recognition) task. Indeed, offering a unified explanation of such seemingly disparate paradigms as paired associates and representativeness is part of the appeal of our approach.

The reason that contextual retrieval is able to explain the representativeness heuristic is that it naturally provides a role for observations in which targets co-occur with decoy distributions. What matters isn't, for example, how many high growth companies turn out to resemble Nvidia, but rather how many low growth companies do not. The futures of low-growth companies erode contextual similarity, even though they have no role in Bayesian reasoning. At the same time, this cognitive mechanism is "almost right" and is thus challenging to correct with conscious effort. This may help explain the persistence of financial anomalies.

Our model successfully demonstrates the role of the kernel of truth and the role of alternative associations, as well as providing an excellent quantitative fit to experimental data. The conjunction fallacy emerges naturally when composite representations simultaneously bring to mind multiple associations. In financial markets, the recognition mechanism accounts for a range of anomalies: negative stub values in equity carve-outs, the price effects of corporate name changes and stock splits, the disconnect between prices and dividends, and the long-standing puzzles of the value premium and excess volatility.

Several avenues for future research emerge from this work. First, the model predicts that the representativeness heuristic arises from the dynamics of paired associates. Further experiments could explore this link. Second, while highly tractable, the model abstracts from essential principles of memory, such as temporal contiguity. Re-introducing these memory features will eventually be important in producing a unified theory. Third, the model may provide the potential to explain other behavioral anomalies, such as the disposition effect (Yeung et al. 2025).

Finally, while the representativeness heuristic leads to systematic errors in probability judgment, it may serve an adaptive function. The examples presented here have as a key feature that they involve asymmetric associations. It may be that in cases where associations are more symmetric, the heuristic does not face these problems and may have advantages in computability. Further work could also elucidate these advantages, pointing to a more general theory of cognition.

**Appendix**

# Questions regarding probability and number 

Throughout the main text, we focus on what the model implies for the relative likelihood of hypotheses---that is, whether an agent judges one hypothesis to be more likely than another. However, the model can be naturally extended to explain a broader range of phenomena, including those in which agents state a probability.

As before, free recall is *not* required---the agent need not generate features from memory. For example, in the (Bordalo et al. 2021) experiment, in which agents are rapidly shown a set of words or numbers, it would not be realistic for subjects to remember specific instances and then count them up. Rather, subjects translate the similarities into probabilities. The Luce choice rule (Luce 1959) provides a natural way to do this.

Let $F(\cdot)$ be an increasing continuous function defined on the non-negative real numbers. For example $F(x) = x^\eta$ for $\eta>0$. Assume the setting in the 1. The Luce choice rule gives the following for elicited probability $\Phat$: $$
\Phat(h|d) = \frac{F(\boldsymbol{x}_h\cdot \boldsymbol{x}_d)}{\sum_{h'\in \calH}F(\boldsymbol{x}_{h'}\cdot \boldsymbol{x}_d)}

$$ If the question pertains to the number of instances, the agents estimate a quantity $\Nhat$ and then apply $\Phat(h|d)\Nhat$. Restricting attention to $F(x) = x^\eta$, the lower is $\eta$, the more elicited probabilities will shrink toward equal probabilities. Regardless of $\eta$, elicited probabilities will be equal if the inner products are equal and will be one or zero as the relative inner products diverge (preserving the results of Section 3.3).

To summarize:

1. Agents form judgments of relative likelihood based on the cosine similarity of the retrieved context vectors (see 1).

2. Agents assess probabilities based on cosine similarity combined with a Luce choice rule.

3. Agents assess quantities by multiplying probability assessments with estimates of the total number of items.

These assumptions suffice to map the associative recognition task into probabilistic judgment. The model could be easily extended to account for processing noise, as in Section 3.4.

These assumptions only rely on subjects understanding that probabilities sum to one and knowing, roughly, the number of items they have seen. It is straightforward to show that, given these assumptions, the model satisfies Predictions 1--3 of (Bordalo et al. 2021). The correlational patterns reported by Bordalo et al. (2021) further support the hypothesis of the same fundamental mechanism driving the qualitative likelihood statement and the quantitative probabilistic and numerical ones.[^20]

However, there are circumstances where these assumptions may not be reasonable. One, described by (Bordalo et al. 2023) and in recent work by (Conlon and Kwon 2025), is that the list of possible hypotheses is not obvious. In that case, free recall most likely comes into play, and the probability of any given item may be biased upward or downward based on what the presence of features does to cue or suppress items during free recall. A second is when subjects are explicitly cued with a probability. Because so much of the literature on probabilistic reasoning involves a probability as a cue, we consider one such case in detail.

One example, frequently cited in the context of the representativeness heuristic is (Casscells et al. 1978). Casscells et al. (1978) asked a group of medical professionals the following question: "If a test to detect a disease whose prevalence is 1/1000 has a false positive rate of 5 percent, what is the chance that a person found to have a positive result actually has the disease, assuming that you know nothing about the person's symptoms or signs?" The correct answer is around 1 in 51 (less than $2\%$): 1 of the 1000 will have an accurate positive test, and 5% of the remaining 999 (about 50 people) will have false positives. The mean response was 55.9% and the modal response, given by 45% of the participants, was 95%.[^21] 18% of the participants gave the correct answer.

This and similar studies (Eddy 1982) are subject to the criticism that they are asking agents to solve a probability problem, whereas in real-life settings, agents form judgements based on their experience. Suppose, however, we were to assume that the example was an accurate representation of cases considered by physicians and stored in their memory. Our model would predict that physicians would give an overstated probability of disease, but one that nonetheless is below 50%. However, there is no reason to believe that the example is an accurate representation; physicians may generally handle conditions with greater prevalence. Moreover, 95% itself represents a cue. Thus subjects, drawing from their memory, believe that the test makes disease more likely than otherwise, and then produce the number that is given to them. (Bordalo et al. 2025) consider several examples of incorrect probabilistic reasoning, emphasizing the importance of the cue.

# Manipulation of recall through cues 

Not surprisingly, this model which is designed to account for the role of cues, also accounts for cue-dependent recall as demonstrated by the third study of (Bordalo et al. 2021). Study 3 manipulates Study 1 by introducing a third attribute to the items: font size.[^22] All subjects are shown 10 large orange numbers, 15 small blue numbers, and 25 large blue words. There are then two treatments. Subjects in the color treatment are asked 18 (what is the likely color of a number) and 18 (what is the probability that a number is orange). Subjects in the size treatment are instead asked about size:

5. "An image was randomly drawn from the images that were just shown to you. The chosen image showed a number. What is the likely font size of a randomly drawn number?" 

6. "An image was randomly drawn from the images that were just shown to you. The chosen image showed a number. What is the probability that a randomly drawn number is large?" 

Regardless of the treatment, the Bayesian response should be the same. The goal of the study is therefore to study the importance of the cue, specifically to test whether the associations formed with the large blue words affect the judgments, despite their irrelevance to the questions. However, (Bordalo et al. 2021) show in the data that

(Bordalo et al. 2021) predict that the in the color treatment, agents are more likely to recall that the item is orange than they are that the item is large in the size treatment, which is in fact what the data show.

Our model makes the same prediction. Intuitively, in the color treatment, the presence of large *blue* words weakens the association between number and blue; whereas in the size treatment, the presence of *large* blue words weakens the association between number and orange (since both are large).

Formally, in the color treatment, the agent evaluates the inner products: $$\boldsymbol{x}_{\textsc{ Blue}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P(\textsc{ Blue},\textsc{ Number})}{\sqrt{P(\textsc{ Blue})P(\textsc{ Number})}} = \frac{15}{\sqrt{15+25}\sqrt{25}},$$ and $$\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P(\textsc{ Orange},\textsc{ Number})}{\sqrt{P(\textsc{ Orange})P(\textsc{ Number})}} = \frac{10}{\sqrt{10}\sqrt{25}}.$$ In the size treatment, the agent instead evaluates $$\boldsymbol{x}_{\textsc{ Small}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P(\textsc{ Small},\textsc{ Number})}{\sqrt{P(\textsc{ Small})P(\textsc{ Number})}} = \frac{15}{\sqrt{15}\sqrt{25}}$$ and $$\boldsymbol{x}_{\textsc{ Large}}\cdot \boldsymbol{x}_{\textsc{ Number}}= \frac{P(\textsc{ Large},\textsc{ Number})}{\sqrt{P(\textsc{ Large})P(\textsc{ Number})}} = \frac{10}{\sqrt{10 + 25}\sqrt{25}}.$$ In the color treatment, the ratio of inner products is $$\frac{\boldsymbol{x}_{\textsc{ Orange}}\cdot \boldsymbol{x}_{\textsc{ Number}}}{\boldsymbol{x}_{\textsc{ Blue}}\cdot \boldsymbol{x}_{\textsc{ Number}}} \approx 1.3,$$ whereas in the size treatment, the corresponding ratio is $$\frac{\boldsymbol{x}_{\textsc{ Large}}\cdot \boldsymbol{x}_{\textsc{ Number}}}{\boldsymbol{x}_{\textsc{ Small}}\cdot \boldsymbol{x}_{\textsc{ Number}}} \approx 0.4.$$ Thus, the model predicts that subjects are more likely to judge the number to be orange in the color treatment versus large in the size treatment. Likewise, under a Luce choice rule, the subjective probability of orange/large will be higher in the color treatment.

# Alternative model fit to (Bordalo et al. 2021) 

In the main text, we estimate $\sigma$ using all moments in Figures 1 and 2 of (Bordalo et al. 2021). Here, we show that we can alternatively calibrate the value of $\sigma^2$ to a single moment: the proportion of subjects who judged orange to be more likely in the gray treatment. From the computations in the main text and Figure 1 of (Bordalo et al. 2021), $\sigma^2$ solves $$P(-0.2027 > \tilde{\epsilon}) = 0.295.$$ Letting $\Phi(z)$ denote the standard normal CDF, this means that[^23] $$\hat{\sigma} = \frac{-0.2027}{\Phi^{-1}(0.295)} \approx 0.3762.$$ Given this calibration, we can then compute the model-implied moments for the blue treatment in Figures 1 and 2 of (Bordalo et al. 2021) from the normal CDF, as described above. Figure 4 compares the data in their Figure 1 to that implied by our model. Figure 5 plots the comparison for their Figure 2.

<figure id="fig:BCGSS_fig1_cal" data-latex-placement="p">
<embed src="../Code/plots/BCGSS_1_cal.pdf" style="width:50.0%" />
<figcaption>Study 1, Figure 1 of <span class="citation" data-cites="Bordetal:21Rep">(Bordalo et al. 2021)</span> The noise parameter <span class="math inline"><em>σ</em></span> is calibrated to match the gray treatment.</figcaption>
</figure>

<figure id="fig:BCGSS_fig2_cal" data-latex-placement="p">
<figure>
<embed src="../Code/plots/BCGSS_2a_cal.pdf" />
<figcaption><span class="citation" data-cites="Bordetal:21Rep">Bordalo et al. (2021)</span> Figure 2a</figcaption>
</figure>
<figure>
<embed src="../Code/plots/BCGSS_2b_cal.pdf" />
<figcaption><span class="citation" data-cites="Bordetal:21Rep">Bordalo et al. (2021)</span> Figure 2b</figcaption>
</figure>
<figcaption>Study 2, Figure 2 of <span class="citation" data-cites="Bordetal:21Rep">(Bordalo et al. 2021)</span> The noise parameter <span class="math inline"><em>σ</em></span> is calibrated to match the gray treatment in Figure 1.</figcaption>
</figure>

Baker, Malcolm, Robin Greenwood, and Jeffrey Wurgler. 2009. "Catering Through Nominal Share Prices." *Journal of Finance*.

Barberis, N., A. Shleifer, and R. Vishny. 1998. *A Model of Investor Sentiment*.

Bhatia, S. 2017. *Associative Judgement and Vector Space Semantics*.

Birru, Justin, and Baolian Wang. 2016. "Nominal Price Illusion." *Journal of Financial Economics*.

Bordalo, P., K. Coffman, N. Gennaioli, F. Schwerter, and A. Shleifer. 2021. *Memory and Representativeness*.

Bordalo, P., K. Coffman, N. Gennaioli, and A. Shleifer. 2016. *Stereotypes*.

Bordalo, P., J. J. Conlon, N. Gennaioli, S. Y. Kwon, and A. Shleifer. 2023. *Memory and Probability*.

Bordalo, P., J. J. Conlon, N. Gennaioli, S. Y. Kwon, and A. Shleifer. 2025. *How People Use Statistics*.

Bordalo, P., N. Gennaioli, R. L. Porta, and A. Shleifer. 2019b. *Diagnostic Expectations and Stock Returns*.

Bordalo, P., N. Gennaioli, R. L. Porta, and A. Shleifer. 2019a. *Diagnostic Expectations and Stock Returns*.

Bordalo, P., N. Gennaioli, and A. Shleifer. 2018. *Diagnostic Expectations and Credit Cycles*.

Bordalo, P., N. Gennaioli, and A. Shleifer. 2020. *Memory, Attention, and Choice*.

Campbell, J. Y., and R. J. Shiller. 1988. *The Dividend-Price Ratio and Expectations of Future Dividends and Discount Factors*.

Casscells, W., A. Schoenberger, and T. B. Graboys. 1978. *Interpretation by Physicians of Clinical Laboratory Results*.

Conlon, J. J., and S. Y. Kwon. 2025. *Beliefs from Cues*.

Cooper, Michael J., Orlin Dimitrov, and P. Raghavendra Rau. 2001. "A Rose.com by Any Other Name." *Journal of Finance*.

Desai, Hemang, and Prem C. Jain. 1997. "Long-Run Common Stock Returns Following Stock Splits and Reverse Splits." *Journal of Business*.

Eddy, D. M. 1982. *Probabilistic Reasoning in Clinical Medicine: Problems and Opportunities*.

Estes, W. K. 1972. *Research and Theory on the Learning of Probabilities*.

Estes, W. K. 1976. *The Cognitive Side of Probability Learning*.

Fama, E. F., and K. R. French. 1992. *The Cross-Section of Expected Returns*.

Gennaioli, N., and A. Shleifer. 2010. *What Comes to Mind*.

Gennaioli, N., and A. Shleifer. 2018. *A Crisis of Beliefs: Investor Psychology and Financial Fragility*.

Gomes, J. F., M. Grotteria, and J. A. Wachter. 2019. *Cyclical Dispersion in Expected Defaults*.

Gourio, F. 2012. *Disaster Risk and Business Cycles*.

Guo, H., and J. A. Wachter. 2025. *"Superstitious" Investors*.

Hall, R. E. 2017. *High Discounts and High Unemployment*.

Hartzmark, Samuel M., and David H. Solomon. 2019. "The Dividend Disconnect." *Journal of Finance*.

Healey, M. K., N. M. Long, and M. J Kahana. 2019. "Contiguity in Episodic Memory." *Psychonomic Bulletin & Review* 26 (3): 699---720.

Hockley, W. E. 1992. "Item Versus Associative Information: Further Comparisons of Forgetting Rates." *Journal of Experimental Psychology: Learning, Memory, and Cognition* 18: 1321--30.

Howard, M. W., and M. J. Kahana. 2002. "A Distributed Representation of Temporal Context." *Journal of Mathematical Psychology* 46 (3): 269--99. <https://doi.org/10.1006/jmps.2001.1388>.

Ikenberry, David L., Graeme Rankine, and Earl K. Stice. 1996. "What Do Stock Splits Really Signal?" *Journal of Financial and Quantitative Analysis*.

Jin, B. J., M. Kahana, and D. J. Halpern. 2024. *A Theory of Memory for Items and Associations*.

Kahana, M. J. 2012. *Foundations of Human Memory*. Oxford University Press.

Kahneman, D., and A. Tversky. 1972. *Subjective Probability: A Judgment of Representativeness*.

Kahneman, D., and A. Tversky. 1973. *On the Psychology of Prediction*.

Kilic, M., and J. A. Wachter. 2018. *Risk, Unemployment, and the Stock Market: A Rare-Event-Based Explanation of Labor Market v*.

La Porta, Rafael. 1996. "Expectations and the Cross-Section of Stock Returns." *Journal of Finance*.

Lamont, Owen A., and Richard H. Thaler. 2003. "Can the Market Add and Subtract? Mispricing in Tech Stock Carve-Outs." *Journal of Political Economy*.

Lettau, M., and J. A. Wachter. 2007. *Why Is Long-Horizon Equity Less Risky? A Duration-Based Explanation of the Value Premium*.

Luce, R. D. 1959. *Individual Choice Behavior*.

Manning, J. R., J. C. Hulbert, J. Williams, L. Piloto, L. Sahakyan, and K. A. Norman. 2016. "A Neural Signature of Contextually Mediated Intentional Forgetting." *Psychonomic Bulletin & Review* 23: 1534--42.

Metcalfe, J. 1991. "Recognition Failure and the Composite Memory Trace in CHARM." *Psychological Review* 98: 529--53. <https://doi.org/10.1037/0033-295X.98.4.529>.

Mullainathan, S. 2002. *A Memory-Based Model of Bounded Rationality*.

Nagel, S., and Z. Xu. 2018. *Asset Pricing with Fading Memory*.

Osth, A. F., and J. Fox. 2019. *Are Associations Formed Across Pairs? A Test of Learning by Temporal Contiguity in Associa*.

Osth, Adam F, and Simon Dennis. 2024. "Global Matching Models of Recognition Memory." In *Oxford Handbook of Human Memory*, edited by Michael J. Kahana and Anthony D. Wagner, vol. 1. Oxford University Press.

Stanislaw, Harold, and Natasha Todorov. 1999. "Calculation of Signal Detection Theory Measures." *Behavior Research Methods, Instruments, & Computers* 31 (1): 137--49. <https://doi.org/10.3758/bf03207704>.

Tversky, A., and D. Kahneman. 1974. *Judgment Under Uncertainty: Heuristics and Biases*.

Tversky, A., and D. Kahneman. 1983. *Extensional Versus Intuitive Reasoning: The Conjunction Fallacy in Probability Judgment*.

Tversky, A, and D Kahneman. 1973. "[Availability: A heuristic for judging frequency and probability]." *Cognitive Psychology* 5 (2): 207--32.

Wachter, J. A., and M. J. Kahana. 2024. *A Retrieved-Context Theory of Financial Decisions*.

Yeung, T. L., R. Liu, J. A. Wachter, M. J. Kahana, and Y. Zhang. 2025. *Navigating Through Fear and Greed: The Experience-Driven Disposition Effect*.

[^1]: Department of Psychology, University of Pennsylvania. kahana@psych.upenn.edu.

[^2]: Stanford University, Graduate School of Business. jparon@stanford.edu.

[^3]: Department of Finance, The Wharton School, University of Pennsylvania, and NBER. jwachter@wharton.upenn.edu

[^4]: We thank Sudeep Bhatia, Pedro Bordalo, Spencer Kwon, Alice Healy, Peter Maxted, Nikolai Roussanov, John Sakon, Yao Zeng, and participants at the Society of Financial Studies Cavalcade, at the Spring 2024 Memory Beliefs and Choice Meeting, at Carnegie Mellon University, London Business School, and the University of Pennsylvania for helpful comments. We have no conflicts to disclose. We are grateful for financial support from NIH grant MH55687.

[^5]: While (Tversky and Kahneman 1973) consider availability as a heuristic distinct from representativeness, and later cite these two as separate when developing a taxonomy of heuristics (Tversky and Kahneman 1974), (Tversky and Kahneman 1983) merge the concepts, as do (Gennaioli and Shleifer 2010). The advantage of a cognitive theory is that it can offer a unified theory for various heuristics.

[^6]: We use the notation $-h, h$ to denote generic distinct elements of $\calH$. In contrast, we use $-d$ to denote $\calD\setminus\{d\}$. This removes the need for unnecessary subscripts. In all of the examples we consider, $\calD$ consists of two elements, which implies that the notation is consistent across $\calD$ and $\calH$. However, nothing in the analysis requires that $\calD$ consist of only two elements.

[^7]: See Wachter and Kahana (2024, fig. 2).

[^8]: The data on free recall and associative recognition can be reconciled by allowing contextual persistence to vary over time. The data strongly suggest such time-variation. It has long been known that context can be "reset," through the use of distractor tasks, and the resetting of context has become a standard element of experimental design (Healey et al. 2019). Resetting of contexts implies that the autoregressive coefficient is temporarily equal to zero. To memorize a pair or a set of features experienced together, it may be optimal for a subject to deliberately orthogonalize a context. The idea that a subject can do this for themselves may be surprising, but neural data suggests it is possible (Manning et al. 2016).

[^9]: More realistically, the dimensionality of features and context spaces is probably on the order of $10^7$ or more, with $10^7$ considered a lower bound on neurons in the brain involved in memory storage. We consider a submatrix of $M$, and the corresponding subvector of features and context.

[^10]: The theorems below highlight the importance of $P(h,{-d})$ in likelihood judgments regarding $P(h,d)$. The importance of $P(h,-d)$ is also recognized by (Bordalo et al. 2021) who explicitly incorporate it into a reduced-form model of probabilities. Appendix 3.5 compares our model with theirs.

[^11]: In the gray treatment, gray could also be considered as a third target. However, because no gray numbers were ever observed, its similarity to the cue is trivially zero, so we ignore it.

[^12]: For gray, the inner product will be zero, so no subject would ever say gray is most likely.

[^13]: In Appendix 9, we also consider a simpler calibration that exactly identifies $\sigma$ from one moment, the gray treatment.

[^14]: This statement is an approximate one because the functional form --) does not nest our results. Rather, our model offers a cognitive foundation for why $P(h,-d)$ would enter the probability assessment of $P(h|d)$.

[^15]: *We use the notation $h_1$ to denote a generic element of $\calH_1$, and similarly $h_2$ to denote a generic element of $\calH_2$ when the second subscript is not necessary for clarity.*

[^16]: The formal structure also maps into the conjunction fallacy of Section 4. Define $\calH_1$ as indexing states regarding Palm's specific business prospects and $\calH_2$ as indexing 3Com's overall solvency. The states in which Palm pays off are the conjunction $h_1 \cap h_2$: Palm succeeds *and* 3Com remains solvent. Under condition ), investors can judge this conjunction as more probable than $h_2$ alone, generating a negative stub value. (Bordalo et al. 2023) cite (Lamont and Thaler 2003) and argue that sub-additivity (state prices summing to more than one) can account for carve-out mispricing. But sub-additivity is weaker than the conjunction fallacy: it says the parts sum to more than the whole, but it does not imply that a conjunction is judged more likely than a component.

[^17]: The price-level channel is ambiguous for reverse splits: the relationship between nominal price and retrieved associations need not be monotonic, as very low prices can retrieve contexts associated with either high-growth potential or financial distress. The event-association channel, by contrast, is unambiguous.

[^18]: This memory database could arise from the analyst organizing historical data at the time of analysis, or through the mechanism of thoughts becoming data (Wachter and Kahana 2024). 

[^19]: See (Guo and Wachter 2025), (Bordalo et al. 2019b), (Gomes et al. 2019), and (Kilic and Wachter 2018) for quantitative models built on biased beliefs about profitability.

[^20]: The link between judgments of likelihood, probability assessments, and numerical assessments is most likely enhanced when subjects are asked these questions as part of the same experiment, as in Bordalo et al. (2021). In this case, the initial answer given by the subject becomes a data point (Wachter and Kahana 2024; Mullainathan 2002) in their memory database.

[^21]: This exhibits kernel of truth because $P(h|d) = P(h,d)/P(d) \approx 0.001/0.05 =1/50$, whereas $P(h) = 1/1000$. Note that we have used $P(h,d) = P(h)$ under the assumption that the false negative rate $P(-d|h) = P(h,-d)/P(h) = 0$; further note $P(d) = P(h,d) + P({-h},d) = 0.001 + 0.05\times 0.999\approx
 0.05$. However, subjects are not reversing conditional probabilities. The model response of 0.95 is $P(h|d)$, nor $P(d|h)$, but rather $P({-d}|{-h})$, or one minus the false positive rate of $P(d|{-h})$.

[^22]: In Study 1, subjects are shown 10 orange numbers, 15 blue numbers, and 25 blue words. After observing the sequence, subjects are asked a series of questions:

 1. "An image was randomly drawn from the images that were just shown to you. The chosen image showed a number. What is the likely color of the chosen image?" 

 2. "An image was randomly drawn from the images that were just shown to you. The chosen image showed a number. What is the probability that the number is orange?" 

 3. "How many orange numbers were shown to you?" 

 4. "How many blue numbers were shown to you?" 

[^23]: The threshold $-0.20$ is $z=\Phi^{-1}(0.3)$ standard deviations $\sigma$ away from zero, so $-0.20 = \sigma z$.
