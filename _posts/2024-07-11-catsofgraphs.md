---
layout: post
title:  The Category of Simple Graphs
date:   July 11, 2024
description: We play around with some simple graphs to get a feel for their category.
tags: graphs, category-theory
categories: math
---

I've been trying to learn more about algorithms and computer science lately, and so wanted to nail down how to do some simple categorical constructions with graphs.

Interestingly, subtleties appear immediately. The biggest one is: what do you mean by a graph?

There's a ton of different notions of graphs, each with their own uses and conventions. For right now, I'm mainly interested in undirected graphs with at most one edge between two vertices and no loops. These kinds of graphs are often called **simple graphs**, and they seem (at least upon my beginner knowledge) to be slightly more central to algorithms and computer science than directed graphs, or graphs with multiple edges (also called multigraphs).

Now there's quite a bit written about this zoo of kinds of graphs, such as the thesis [The Categories of Graphs](https://scholarworks.umt.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1986&context=etd)[^1] and this [nlab page](https://ncatlab.org/nlab/show/graph), so I won't talk too much about it. Here's a table summarizing the graphs in the nlab article.

| Graph | directed | multiple edges | loops |
| - | - | - | - |
| simple graph | No | No | No |
| multigraph | No | Yes | No |
| loop graph | No | No | $$\leq 1$$ |
| pseudograph | No | Yes | Yes |
| directed graph | Yes | No | No |
| directed multigraph | Yes | Yes | No |
| directed loop graph | Yes | No | $$\leq 1$$ |
| directed pseudograph | Yes | Yes | Yes |

**Caveat:** Pseudographs can have *multiple loops* on a vertex. We assume (directed) loop graphs can have at most *one* loop on a vertex.

Category theorists are probably most used to working with directed pseudographs, since categories are directed pseudographs with extra structure (identity loops and composition).

Right off the bat, let us note that the category $$\mathsf{DPGrph}$$ of directed pseudographs is super nice. Indeed, if we let $$(* \rightrightarrows *)$$ denote the category with two objects $$E$$ and $$V$$ and two non-identity morphisms $$s, t : E \to V$$, then a directed pseudograph is the same thing as a functor $$G : (* \rightrightarrows *) \to \mathbf{Set}$$. Thus $$\mathsf{DPGrph} = \mathbf{Set}^{* \rightrightarrows *}$$ is a Grothendieck topos, in particular it is a copresheaf category, really the nicest kind of category around. Doing any sort of construction in this category should be dumb simple, as (co)limits in copresheaf categories are computed objectwise[^2].

So let's get into the math. By a simple graph $$G$$, what I mean is a set $$V(G)$$ of **vertices** equipped with a binary, irreflexive, symmetric relation $$(E(G) \subseteq V(G)^2)$$, called the **edge relation**. So if $$u,v \in V$$, then $$(u,v) \in E(G)$$, which we will also write as $$uv$$ or $$u \sim v$$ if there is an edge connecting $$u$$ and $$v$$.

A map $$f: G \to G'$$ of simple graphs is a function $$V(f): V(G) \to V(G')$$ such that if $$uv \in E(G)$$, then $$f(u)f(v) \in E(G')$$. This gives us the category $$\mathsf{Grph}$$ of simple graphs.

But wait...is this actually what we want? There's a small, kind of annoying thing we notice right away from this definition. With the above definition, the two inclusions $$* \to [*-*]$$ of a simple graph with one vertex and no edges into the simple graph with two vertices and one edge are morphisms, which is good. However, there is **no** morphism in the other direction $$[*-*] \to *$$. This is because if we call the first graph $$G$$ with vertices $$u$$ and $$v$$ and the second graph $$G'$$ with single vertex $$w$$, then $$uv \in E(G)$$, but since $$E(G')$$ is irreflexive, $$ww \notin E(G')$$. Thus the function sending $$u$$ and $$v$$ to $$w$$ does not define a morphism of simple graphs.

So basically, with the most naive definition above, morphisms of simple graphs cannot collapse edges. Now this might be reasonable for your particular use case, but I don't know, I'd like to consider some cases where you can collapse edges, that seems more natural and fun to me[^4].

Alright, so let's redo this. Lets redefine a simple graph $$G$$ to consist of a set $$V(G)$$ of vertices and a binary, **reflexive**, symmetric relation $$(E(G) \subseteq V(G)^2)$$. So technically, these are different mathematical objects. You might visualize them as undirected graphs with unique edges and where every vertex has exactly one loop. But this is kinda silly. I can't map these loops to anything other than the unique loop where I send the underlying vertex to, so it might as well be like they aren't there. It makes more sense to just identify these with the intuitive notion of a simple graph: undirected, unique edges, no loops, and just allow morphisms to collapse edges. Lets call the objects of $$\mathsf{Grph}$$ just *graphs* from now on.

Let's use the same notion we described as above for morphisms, and use the same name $$\mathsf{Grph}$$. Okay, now this is a nice category. I can visualize its objects easily, its got a concrete mathematical description, and its got some nice morphisms. So let's see how to compute some limits and colimits here.

Now if you check the [nlab page for simple graphs](https://ncatlab.org/nlab/show/category+of+simple+graphs), you'll see a fancy result identifying $$\mathsf{Grph}$$ as a Grothendieck quasitopos, which is a very nice category. For this post, let's just do things by hand to get a feel for this category. But from this abstract result, we know that $$\mathsf{Grph}$$ has all limits, colimits and is cartesian closed.

Note that making even small changes to this definition can have pretty drastic consequences categorically. For example, if we kept the definition before, where we weren't allowed to smush edges, then we end up with a category that doesn't even have all pushouts! See [Spined Categories by Bumpus and Kocsis Page 7](https://arxiv.org/abs/2104.01841).

Also note that Wikipedia considers for its [definition of graph homomorphism](https://en.wikipedia.org/wiki/Graph_homomorphism) to be loop graphs with maps between them that aren't allowed to collapse loops or edges.

First off, lets notice there is a nice functor $$V : \mathsf{Grph} \to \mathbf{Set}$$ that sends a graph to its set of vertices. If I have a map of graphs, then I get a map of their corresponding sets of vertices. This functor has a left adjoint $$\text{Disc} : \mathbf{Set} \to \mathsf{Grph}$$ that sends a set $$S$$ to the graph $$\text{Disc}(S)$$, which has $$V(\text{Disc}(S)) = S$$ and $$E(\text{Disc}(S)) = \varnothing$$[^3]. In other words $$\text{Disc}(S)$$ is the **discrete graph** on the set $$S$$. Now $$V$$ also has a right adjoint $$\text{CoDisc}: \mathbf{Set} \to \mathsf{Grph}$$ which sends a set $$S$$ to the graph $$\text{CoDisc}(S)$$, whose set of vertices is $$S$$, and where every pair of vertices is connected by an edge.

Okay, so $$V$$ has left and right adjoints, so that means it preserves whatever (co)limits exist in $$\mathsf{Grph}$$, and we know what (co)limits in $$\mathbf{Set}$$ look like. So if we take a (co)imit $$\lim_i G_i$$ of graphs, we know that $$V(\lim_i G_i) \cong \lim_i V(G_i)$$. So that helps us guess what (co)limits should be in $$\mathsf{Grph}$$.

Given graphs $$G$$ and $$H$$, let $$G \times H$$ denote the graph with $$V(G \times H) = V(G) \times V(H)$$ and $$E(G \times H) \subseteq V(G \times H)^2$$ is the relation where $$(g,h) \sim_{G \times H} (g',h')$$ if $$g \sim_G g'$$ and $$h \sim_H h'$$. There are maps $$\pi_G : G \times H \to G$$ in $$\mathsf{Grph}$$, with $$\pi_G(g,h) = g$$ and $$\pi_H : G \times H \to H$$, with $$\pi_H(g,h) = h$$. 

**Lemma**: $$G \times H$$ is the product of $$G$$ and $$H$$ in the category $$\mathsf{Grph}$$.

**Proof**: Suppose that we have maps $$g : Q \to G$$ and $$h: Q \to H$$. We want to define a map $$k : Q \to G \times H$$ such that $$\pi_G k = g$$ and $$\pi_H k = h$$. Let $$k(q) = (g(q), h(q))$$. Now this is a map of graphs, because if $$q \sim q'$$, then $$g(q) \sim g(q')$$ and $$h(q) \sim h(q')$$ since $$g$$ and $$h$$ are maps of graphs, and so $$k(q) = (g(q), h(q)) \sim (g(q'),h(q')) = k(q')$$. It is easy to check that this is the unique map such that $$\pi_G k = g$$ and $$\pi_H k = h$$, and hence is the categorical product. $$\square$$

Now let us try coproducts. 

Given graphs $$G$$ and $$H$$, let $$G + H$$ denote the graph with $$V(G + H) = V(G) + V(H)$$ and $$E(G + H)$$ is the relation where $$v \sim_{G + H} v'$$ if $$v, v' \in G$$ and $$v \sim_G v'$$ or $$v,v' \in H$$ and $$v \sim_H v'$$. There are inclusion maps $$i_G : G \to G + H$$ and $$i_H : H \to G + H$$.

**Lemma**: $$G + H$$ is the coproduct of $$G$$ and $$H$$ in the category $$\mathsf{Grph}$$.

The proof is the same idea as for products.

I'll also leave it to you to check that $$\varnothing$$, the graph with no vertices, is the intial object in $$\mathbf{Grph}$$ and $$*$$, the graph with one vertex, is the terminal object in $$\mathbf{Grph}$$.

Now for pushouts. Given maps of graphs $$f: A \to B$$ and $$g: A \to C$$, let $$B+_A C$$ denote the graph with $$V(B +_A C) = V(B) +_{V(A)} V(C)$$, (i.e. $$V(B +_A C)$$ is the set $$V(B) + V(C)$$ quotiented by the equivalence relation $$\simeq$$ where $$v \simeq w$$ if there exist $$a \in V(A)$$ such that $$v = f(a)$$ and $$w = g(a)$$) and let $$E(B +_A C)$$ be defined as follows. If $$x,y \in V(B +_A C)$$, then $$x \sim_{B +_A C} y$$ if there exists $$v,v' \in V(B)$$ with $$v \sim_B v'$$, $$[v] = x$$ and $$[v'] = y$$ or $$w,w' \in V(C)$$ with $$w \sim_C w'$$, $$[w] = x$$ and $$[w'] = y$$. In other words, there is an edge between $$[v]$$ and $$[w]$$ if there is some representative edge in $$B$$ or $$C$$.

There are maps $$i_B : B \to B+_A C$$ and $$i_C : C \to B +_A C$$ given by inclusion.

$$
\begin{CD}
 A @>g>> C\\
 @VfVV @Vi_CVV \\
 B @>i_B>> B+_A C
\end{CD}
$$

**Lemma**: $$B+_A C$$ is the pushout of $$f$$ and $$g$$ in $$\mathsf{Grph}$$.

**Proof**: Suppose that we have maps $$n : B \to Q$$ and $$m : C \to Q$$ such that $$nf = mg$$. We want to define a map $$k : B+_A C \to Q$$ such that $$k i_B = n$$ and $$k i_C = m$$. On vertices, define it as you would in $$\mathsf{Set}$$, i.e. send $$x \mapsto n(x)$$ if $$x = [b]$$ for some $$b \in B$$ and $$x \mapsto m(x)$$ if $$x = [c]$$ for some $$c \in C$$. If $$[b] = [c]$$, then there exists an $$a\in A$$ with $$f(a) = b$$ and $$g(a) = c$$, so $$n(b) = nf(a) = mg(a) = m(c)$$. So our map $$k$$ is well defined. If $$[v] \sim_{B+_A C} [w]$$, then $$k[v] \sim_Q k[w]$$, because in order for $$[v] \sim [w]$$, there has to be some representative of the edge in $$B$$ or $$C$$, and $$n$$ and $$m$$ preserve the edges of $$B$$ and $$C$$ respectively. Its now not hard to see that $$k$$ satisfies the necessary properties for $$B +_A C$$ to be a pushout.

Note that this is a generalization of the well-known [clique sum construction](https://en.wikipedia.org/wiki/Clique-sum) in graph theory.

Finally, let's look at pullbacks.

Given maps $$f : A \to B$$ and $$g: A \to C$$ of graphs, let $$B \times_A C$$ denote the graph with $$V(B \times_A C) = V(B) \times_{V(A)} V(C)$$ and with $$E(B \times_A C)$$ defined as follows. We have $$(b,c) \sim_{B \times_A C} (b',c')$$ if $$b \sim_B b'$$ and $$c \sim_C c'$$.

**Lemma**: $$B \times_A C$$ is the pullback of $$f$$ and $$g$$ in $$\mathsf{Grph}$$.

**Proof**: Suppose we have maps $$n : Q \to B$$ and $$m : Q \to C$$ such that $$fn = gm$$. We want to define a map $$k : Q \to B\times_A C$$ such that $$\pi_B k = n$$ and $$\pi_C k = m$$. Well define $$k(q) = (n(q), m(q))$$. Its now easy to check that since $$n$$ and $$m$$ preserve edges that $$k$$ will as well, and it's clearly unique and satisfies the required conditions.

So the basic categorical constructions for $$\mathsf{Grph}$$ are pretty straightforward and nice. It would be interesting to compare this to all these other kinds of categories of graphs! 

___


Fun aside that I haven't really thought through too much: If we consider the category $$\mathsf{orGrph}$$, whose objects are simple graphs with an ordering on their vertices, then we get a cosimplicial object $$K^\bullet : \mathsf{\Delta} \to \mathsf{orGrph}$$ given by the cliques and inclusion or collapse maps between them. Anytime we have such a cosimplicial object in a cocomplete category, we get an adjunction $$\text{Re}: \mathsf{sSet} \rightleftarrows \mathsf{orGrph} : \text{Sing}$$. In this case, if $$G$$ is a graph, then $$\text{Sing}(G)$$ is a simplicial set gotten by mapping cliques into $$G$$. The homotopy type of $$\text{Sing}(G)$$ is thus the same as the [clique complex](https://en.wikipedia.org/wiki/Clique_complex) of $$G$$. Neat! Then $$\text{Re}$$ is like gluing cliques together according to a simplicial set "recipe." 

[^1]: In this reference, all of these examples of graphs are derived from a more general structure, which they call a *conceptual graph*.

[^2]: See Riehl's [Category Theory in Context](https://math.jhu.edu/~eriehl/context.pdf) Proposition 3.3.9 for a more precise description of what I mean.

[^3]: Technically it should be $$E(F(S)) = \Delta_{S}$$, the diagonal, i.e. the set $$\Delta_S = \{ (s, s) \in S \times S \}$$ since we are asking for the edge relation to be reflexive, but going forward, let's just ignore these "ghost edges."

[^4]: However we do lose something really important when we use these morphisms and not the more strict ones. If we let $$K^n$$ denote the $$n$$-clique, i.e. the complete graph on $$n$$ vertices, then with the strict morphisms that don't collapse edges, maps of graphs $$G \to K^n$$ are equivalent to $$n$$-colorings of $$G$$. If we allow morphisms to collapse edges, then there are always such maps, we can just collapse everything to a single vertex for instance, so we lose the correspondence.