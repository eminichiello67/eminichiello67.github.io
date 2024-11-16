---
layout: post
title: Pushouts along monomorphisms.
date: November 14, 2024
description: A quick post to discuss adhesive categories.
tags: graphs, category-theory
categories: math
---

Continuing on with the previous blog posts about categories of simple graphs, let us talk about a special class of categories, called **adhesive categories** and show that $$\mathsf{rGrph}$$ belongs to this class.

Let's start with the definition:
A category $$\mathcal{C}$$ is **adhesive** if

* it has pullbacks, and
* pushouts along monomorphisms[^1] exist and are Van Kampen.

Okay, so this might seem a little weird at first glance. What exactly does it mean for pushouts along monomorphisms to be Van Kampen? What does that have to do with graphs? All in due time, be patient!

First, let's discuss Van Kampen colimits. This is a topic that really deserves a blog post of its own, so I'll only give some basic details. We say a diagram $$d: I \to \mathcal{C}$$ has a **Van Kampen** colimit if the colimit of $$d$$ exists and there is an equivalence
$$ \mathcal{C}_{/\text{colim}_i \, d(i)} \simeq \lim_i \mathcal{C}_{/d(i)},$$
where on the right hand side we have a pseudolimit. 

The big idea here is: a diagram's colimit is Van Kampen if you can "get the pieces back after you glued them together."

Both the equivalence above and that vague statement might leave you feeling angry, and I understand. Here's a much more concrete way to think about this in the case when the diagram is a pushout.

So suppose we have a diagram $$Y_0 \xleftarrow{g_0} Y_1 \xrightarrow{g_1} Y_2$$
and let $$Y = Y_0 +_{Y_1} Y_2$$ be its colimit, i.e. pushout. Suppose we have a map $$\alpha : X \to Y$$, and we take pullbacks
<!-- https://q.uiver.app/#q=WzAsNixbMSwxLCJZIl0sWzEsMCwiWCJdLFswLDEsIllfMCJdLFsyLDEsIllfMiJdLFswLDAsIlhfMCJdLFsyLDAsIlhfMiJdLFsxLDAsIlxcYWxwaGEiLDJdLFsyLDAsIlxcbGFtYmRhXzAiLDJdLFszLDAsIlxcbGFtYmRhXzIiXSxbNCwyLCJcXGFscGhhXzAiLDJdLFs0LDEsIlxcc2lnbWFfMCJdLFs1LDMsIlxcYWxwaGFfMiJdLFs1LDEsIlxcc2lnbWFfMiIsMl0sWzQsMCwiIiwwLHsic3R5bGUiOnsibmFtZSI6ImNvcm5lciJ9fV0sWzUsMCwiIiwwLHsic3R5bGUiOnsibmFtZSI6ImNvcm5lciJ9fV1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNixbMSwxLCJZIl0sWzEsMCwiWCJdLFswLDEsIllfMCJdLFsyLDEsIllfMiJdLFswLDAsIlhfMCJdLFsyLDAsIlhfMiJdLFsxLDAsIlxcYWxwaGEiLDJdLFsyLDAsIlxcbGFtYmRhXzAiLDJdLFszLDAsIlxcbGFtYmRhXzIiXSxbNCwyLCJcXGFscGhhXzAiLDJdLFs0LDEsIlxcc2lnbWFfMCJdLFs1LDMsIlxcYWxwaGFfMiJdLFs1LDEsIlxcc2lnbWFfMiIsMl0sWzQsMCwiIiwwLHsic3R5bGUiOnsibmFtZSI6ImNvcm5lciJ9fV0sWzUsMCwiIiwwLHsic3R5bGUiOnsibmFtZSI6ImNvcm5lciJ9fV1d&embed" width="432" height="304" style="border-radius: 8px; border: none;"></iframe>

This is like "breaking X into pieces." We then take two more pullbacks to obtain a big commutative cube
<!-- https://q.uiver.app/#q=WzAsOCxbMiwzLCJZIl0sWzIsMSwiWCJdLFswLDMsIllfMCJdLFszLDIsIllfMiJdLFswLDEsIlhfMCJdLFszLDAsIlhfMiJdLFsxLDAsIlhfMSJdLFsxLDIsIllfMSJdLFsxLDAsIlxcYWxwaGEiLDEseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbMiwwLCJcXGxhbWJkYV8wIiwxXSxbMywwLCJcXGxhbWJkYV8yIiwxXSxbNCwyLCJcXGFscGhhXzAiLDIseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbNCwxLCJcXHNpZ21hXzAiLDEseyJsYWJlbF9wb3NpdGlvbiI6NzB9XSxbNSwzLCJcXGFscGhhXzIiXSxbNSwxLCJcXHNpZ21hXzIiLDFdLFs0LDAsIiIsMCx7InN0eWxlIjp7Im5hbWUiOiJjb3JuZXIifX1dLFs2LDQsImZfMCIsMl0sWzYsNSwiZl8xIl0sWzcsMiwiZ18wIiwyXSxbNywzLCJnXzEiLDAseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbNiw3LCJcXGFscGhhXzEiLDEseyJsYWJlbF9wb3NpdGlvbiI6NzB9XSxbNiwzLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XSxbNiwxMSwiIiwxLHsibGV2ZWwiOjEsInN0eWxlIjp7Im5hbWUiOiJjb3JuZXIifX1dLFs1LDgsIiIsMCx7ImxldmVsIjoxLCJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsOCxbMiwzLCJZIl0sWzIsMSwiWCJdLFswLDMsIllfMCJdLFszLDIsIllfMiJdLFswLDEsIlhfMCJdLFszLDAsIlhfMiJdLFsxLDAsIlhfMSJdLFsxLDIsIllfMSJdLFsxLDAsIlxcYWxwaGEiLDEseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbMiwwLCJcXGxhbWJkYV8wIiwxXSxbMywwLCJcXGxhbWJkYV8yIiwxXSxbNCwyLCJcXGFscGhhXzAiLDIseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbNCwxLCJcXHNpZ21hXzAiLDEseyJsYWJlbF9wb3NpdGlvbiI6NzB9XSxbNSwzLCJcXGFscGhhXzIiXSxbNSwxLCJcXHNpZ21hXzIiLDFdLFs0LDAsIiIsMCx7InN0eWxlIjp7Im5hbWUiOiJjb3JuZXIifX1dLFs2LDQsImZfMCIsMl0sWzYsNSwiZl8xIl0sWzcsMiwiZ18wIiwyXSxbNywzLCJnXzEiLDAseyJsYWJlbF9wb3NpdGlvbiI6MzB9XSxbNiw3LCJcXGFscGhhXzEiLDEseyJsYWJlbF9wb3NpdGlvbiI6NzB9XSxbNiwzLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XSxbNiwxMSwiIiwxLHsibGV2ZWwiOjEsInN0eWxlIjp7Im5hbWUiOiJjb3JuZXIifX1dLFs1LDgsIiIsMCx7ImxldmVsIjoxLCJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0=&embed" width="560" height="560" style="border-radius: 8px; border: none;"></iframe>

So each of the four faces around the cube are pullbacks and the bottom of the cube is a pushout. We say that the diagram has a **universal colimit** if the top face is a pushout. The idea here being that if you take a map $$\alpha : X \to Y$$, where $$Y$$ is glued together from some stuff, and you break $$X$$ apart on the pieces of $$Y$$, then we can glue together those pieces to obtain $$X$$. 

Now if we have a diagram $$Y_0 \xleftarrow{g_0} Y_1 \xrightarrow{g_1} Y_2$$ such that for every diagram $$X_0 \xleftarrow{f_0} X_1 \xrightarrow{f_1} X_2$$ and maps $$\alpha_0 : X_0 \to Y_0, \alpha_1 : X_1 \to Y_1$$ and $$\alpha_2 : X_2 \to Y_2$$ that define a natural transformation such that each commutative square is a pullback (which we call a cartesian natural transformation), and we consider the resulting map $$\alpha : X \to Y$$ where $$X = X_0 +_{X_1} X_2$$ and $$Y = Y_0 +_{Y_1} Y_2$$, then we say that it the diagram has an **effective colimit** if $$X_0 \cong Y_0 \times_{Y} X$$, $$X_1 \cong Y_1 \times_{Y} X$$ and $$X_2 \cong Y_2 \times_{Y} X$$. In other words, given some pieces, we glue them together and break them apart again to get the original pieces.

A colimit is Van Kampen precisely when it is universal and effective. Here's a fun exercise: Show that the category $$\mathbf{Set}$$ does not have all effective pushouts. In other words, not all of $$\mathbf{Set}$$'s colimits are Van Kampen! When I first heard this I was quite surprised, because I thought $$\mathbf{Set}$$ is the best category ever. It turns out, and I won't be precise here, but the problem here is not really with $$\mathbf{Set}$$. Instead, the problem is that we are only looking at $$1$$-categories. It turns out that having all colimits being Van Kampen is precisely what defines an $$\infty$$-topos[^2].

However, $$\mathbf{Set}$$ does have Van Kampen pushouts when the maps $$g_0, g_1$$ in the diagram $$Y_0 \xleftarrow{g_0} Y_1 \xrightarrow{g_1} Y_2$$ are monomorphisms. This is the property of $$\mathbf{Set}$$ that we generalize to define adhesive categories.

Let us show that $$\mathbf{rGrph}$$ is adhesive. So first let's show that $$\mathbf{rGrph}$$ has all pullbacks. Suppose that $$f: B \to A$$ and $$g: C \to A$$ are maps in $$\mathbf{rGrph}$$. Consider the pullback 
<!-- https://q.uiver.app/#q=WzAsNCxbMCwwLCJQIl0sWzAsMSwiQiJdLFsxLDEsIkEiXSxbMSwwLCJDIl0sWzAsMSwicCIsMl0sWzAsMywicSJdLFszLDIsImciXSxbMSwyLCJmIiwyXSxbMCwyLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwwLCJQIl0sWzAsMSwiQiJdLFsxLDEsIkEiXSxbMSwwLCJDIl0sWzAsMSwicCIsMl0sWzAsMywicSJdLFszLDIsImciXSxbMSwyLCJmIiwyXSxbMCwyLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0=&embed" width="304" height="304" style="border-radius: 8px; border: none;"></iframe>

in $$\mathbf{Grph}$$. So $$V(P) = V(B \times_A C) = V(B) \times_{V(A)} V(C)$$, and $$p : P \to B$$ sends $$(b,c) \mapsto b$$. There is an edge $$(b,c) \sim (b', c')$$ iff $$b \sim b'$$ and $$c \sim c'$$, so clearly $$p$$ and $$q$$ do not collapse edges. Therefore the pullback $$P$$ exists in $$\mathbf{rGrph}$$ and agrees with the pullback in $$\mathbf{Grph}$$.

Now we wish to show that pushouts of monomorphisms exist in $$\mathbf{rGrph}$$. Let $$f : A \hookrightarrow B$$ and $$g: A \hookrightarrow C$$ be monomorphisms, and consider the pushout of $$f$$ and $$g$$ in $$\mathbf{Grph}$$
<!-- https://q.uiver.app/#q=WzAsNCxbMCwwLCJBIl0sWzAsMSwiQiJdLFsxLDAsIkMiXSxbMSwxLCJCK19BQyJdLFswLDEsImYiLDIseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDIsImciLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6ImJvdHRvbSJ9fX1dLFsxLDMsIm0iLDJdLFsyLDMsIm4iXSxbMywwLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwwLCJBIl0sWzAsMSwiQiJdLFsxLDAsIkMiXSxbMSwxLCJCK19BQyJdLFswLDEsImYiLDIseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDIsImciLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6ImJvdHRvbSJ9fX1dLFsxLDMsIm0iLDJdLFsyLDMsIm4iXSxbMywwLCIiLDEseyJzdHlsZSI6eyJuYW1lIjoiY29ybmVyIn19XV0=&embed" width="347" height="304" style="border-radius: 8px; border: none;"></iframe>

Let us first show that $$m$$ and $$n$$ are monomorphisms. Suppose that $$b, b' \in B$$ and $$m(b) = m(b')$$. This means that $$[b] = [b']$$, which implies that there exist elements $$a, a_0, \dots, a_n, a'$$ and $$c_0, b_0, \dots, b_n, c_n$$ such that $$f(a) = b$$, $$g(a) = c_0$$, $$g(a_0) = c_0$$, $$f(a_0) = b_0$$, $$\dots$$, $$g(a_n) = c_n$$, $$g(a') = c_n$$, $$f(a') = b'$$. But since $$g$$ is a monomorphism, $$a = a_0$$, so then $$f(a) = b = f(a_0) = b_0$$, and so on, which implies that $$b = b'$$. Thus $$m$$ is a monomorphism. A similar argument holds for $$n$$.

Now since $$m$$ and $$n$$ are monomorphisms, they cannot squash vertices. Similarly, by the description of $$B+_A C$$, $$m$$ and $$n$$ do not squash edges. Therefore the pushout in $$\mathbf{rGrph}$$ exists and agrees with the pushout in $$\mathbf{Grph}$$. 


Suppose that we have monomorphisms $$H_0 \xleftarrow{g_0} H_1 \xrightarrow{g_1} H_2$$ and we let $$H = H_0 +_{H_1} H_2$$ be their pushout. Let $$\alpha : G \to H$$ be a map of graphs, and let $$G_i = H_i \times_H G$$ be respective pullbacks for $$i = 0, 1, 2$$. We want to show that $$G \cong G_0 +_{G_1} G_2$$. Because $$\mathbf{Set}$$ is adhesive, its easy to see that $$V(G) \cong V(G_0 +_{G_1} G_2)$$. Showing that the edges agree is not hard to show. So $$\mathbf{rGrph}$$ is adhesive.

Adhesive categories are a great abstraction for DPO rewriting, which is a framework for graph rewriting. The idea is that one wishes to replace a subgraph with a different graph in a uniform way. You can learn more about adhesive categories from this [wonderful paper of Lack and Sobocinski](https://www.ioc.ee/~pawel/papers/adhesive.pdf).



---
[^1]: Technically an adhesive category is one where you have Van Kampen pushouts when one of the two maps is a monomorphism. For our case however we need both maps to be monos. So maybe it would be better to call these bi-adhesive categories or something, but let's just stick with the adhesive terminology for now.
[^2]: See [here](https://www.math.uwo.ca/faculty/kapulkin/seminars/hottestfiles/Anel-2019-05-2-HoTTEST.pdf) for more.


