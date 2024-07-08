---
layout: post
title:  Diffeological Spaces, Part 3
date:   June 27, 2023
description: The definition of diffeological spaces
tags: diffeological_spaces
categories: math
---

Let us now finally delve into the definition of a diffeological space. Before we do that, we need some preliminary notions.

**Definition**: A **cartesian space** is a finite dimensional smooth manifold diffeomorphic to $$\mathbb{R}^n$$ for some $$n \geq 0$$. Given a set $$X$$, a **parametrization** is a set function $$p : U \to X$$ where $$U$$ is a cartesian space. If $$M$$ is a finite dimensional smooth manifold, and $$\mathcal{U} = \{ U_i \subseteq M \}$$ is a collection of subsets of $$M$$, we say that $$\mathcal{U}$$ is a **good open cover** if each $$U_i$$ is a cartesian space, every finite intersection $$U_{i_0} \cap \dots \cap U_{i_n}$$ is either empty or a cartesian space, and $$\bigcup_i U_i = M$$.

**Definition**[^1]: Given a set $$X$$, a **diffeology** $$\mathcal{D}_X$$ on $$X$$ consists of a set of parametrizations $$p: U \to X$$ satisfying the following three conditions:
1. All parametrizations with domain $$\mathbb{R}^0$$ belong to $$\mathcal{D}_X$$, namely all the points of $$X$$,
2. If $$p : V \to X$$ is a parametrization, and $$f: U \to V$$ is a smooth map between cartesian spaces, then the composition $$p \circ f$$ belongs to $$\mathcal{D}_X$$,
3. If $$p: U \to X$$ is a parametrization, $$\mathcal{U} = \{ U_i \subseteq U \}$$ is a good open cover of $$U$$ and $$p \vert_{U_i} \in \mathcal{D}_X$$ for every $$U_i \in \mathcal{U}$$, then $$p \in \mathcal{D}_X$$.
If $$\mathcal{D}_X$$ is a diffeology, then we call a parametrization $$ p : U \to X$$ that belongs to $$\mathcal{D}_X$$ a **plot**. A **diffeological space** consists of a pair $$(X, \mathcal{D}_X)$$ of a set equipped with a diffeology. 

Given two diffeological spaces $$(X, \mathcal{D}_X)$$ and $$(Y, \mathcal{D}_Y)$$, a **smooth map** between them consists of a set function $$f : X \to Y$$ such that if $$ p : U \to X$$ is a plot of $$X$$, namely $$p \in \mathcal{D}_X$$, then the composite map $$ U \xrightarrow{p} X \xrightarrow{f} Y$$ is a plot of $$Y$$. Let $$\mathsf{Diff}$$ denote the category of diffeological spaces with smooth maps.

Notice how simple these definitions are compared to the corresponding definitions of a smooth manifold! Really think about it, the definition of a manifold is really complicated. Its a kind of topological space (Hausdorff, second-countable), and it has all of these charts, which are homeomorphisms from cartesian spaces, and those charts have to be compatible in some way that's really annoying to write symbolically, and then we consider the biggest collection (maximal atlas) of such charts compatible with the ones you've got, and then you call that a smooth structure. Okay, maybe if you are a seasoned differential geometer it isn't so bad, but I remember spending *months* understanding the definition of a smooth manifold the first time I learned about it. There are so many nooks and crannies to get stuck on it. The definition of a diffeological space however, by comparison is clean and tidy. Same for the definition of smooth map.

Okay, that's nice and all, but its just a definition. I can define whatever the hell I want, but its only interesting if it connects with things I care about. Well, suppose that $$M$$ is a finite dimensional smooth manifold in classical differential geometry. Then we can consider the set $$\mathcal{D}_M$$ of those parametrizations $$ p : U \to M$$ that are smooth as maps of smooth manifolds, in the sense of classical differential geometry. It turns out that $$\mathcal{D}_M$$ satisfies the axioms of a diffeology. In other words, every finite dimensional smooth manifold is canonically a diffeological space. We call this the **manifold diffeology** on $$M$$.

Even more powerfully, a function $$f: M \to N$$ between finite dimensional smooth manifolds is smooth in the classical sense if and only if it is a smooth map in the sense of diffeological spaces between $$M$$ and $$N$$ equipped with their manifold diffeologies! This is proven in the [diffeology textbook](https://www.google.com/books/edition/Diffeology/Nb0xAAAAQBAJ?hl=en) in Article 4.3, and it implies that assigning the manifold diffeology to a manifold defines a fully faithful functor from the category of finite dimensional smooth manifolds to the category of diffeological spaces. 

$$ \mathcal{D}_{(-)} : \mathsf{Man} \hookrightarrow \mathsf{Diff}.$$

Intuitively, this means that we lose nothing by considering manifolds as diffeological spaces via their manifold diffeology. We could also characterize finite dimensional smooth manifolds as those diffeological spaces which have local diffeomorphisms to a fixed $$\mathbb{R}^n$$ and satisfy some additional conditions. 


I think this is a really powerful, and quite different way to think about smooth spaces. For smooth manifolds, we typically fix an atlas (a collection of compatible charts) and root around in the charts, making constructions and then checking that they are independent of the chart we chose. Much of the machinery of an introductory class in differential geometry is devoted to developing technology that hides the complexity of this "chartwise" thinking. 

For diffeological spaces, we don't think about charts at all. Instead we do constructions "plotwise." It might not sound like we've really achieved all that much, just substituted chart for plot, but in doing so, we've actually obtained something really interesting and different.



---
[^1]: The astute reader will note that this is not the definition of a diffeogical space as given in the ["Diffeology textbook"](https://www.google.com/books/edition/Diffeology/Nb0xAAAAQBAJ?hl=en). However, in [my paper](https://arxiv.org/abs/2202.11023), I prove that the category of diffeological spaces as given in the Diffeology textbook and the category of diffeological spaces as given in the definition above are equivalent. The above definition is far more convenient to work with for my purposes.