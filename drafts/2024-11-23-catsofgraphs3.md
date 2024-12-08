---
layout: post
title:  The Category of Simple Graphs, Pt. 3
date:   November 23, 2024
description: We play around with some simple graphs to get a feel for their category.
tags: graphs, category-theory
categories: math
---

I've spent some time now playing around with different categories of graphs. This culminated in a talk I gave at the NYC Category theory seminar. You can find a video of it [here](https://www.youtube.com/watch?v=EOjeZ_5Xbls&t=2317s). I've already learned a lot, even since then. This is mainly due to some great conversations with Ben Bumpus. I wanna share some of these new understandings, and also just have a place to collect my thoughts.

I want to distinguish the following categories:
* Directed pseudographs - morphisms don't collapse edges - topos,
* Directed symmetric pseudographs - morphisms don't collapse edges - topos,
* Simple graphs - morphisms don't collapse edges - crappy category,
* Simple graphs - morphisms can collapse edges - quasitopos.

For the definitions of these different kinds of graphs, see the first blog post in this series. We can think of the last category equivalently as the category whose objects are symmetric, reflexive binary relations on a set, and the second to last category as symmetric, irreflexive binary relations on a set. In both cases, morphisms preserve the relation. The second to last category I've been calling $\mathsf{rGrph}$ and the last $\mathsf{Grph}$.

Ben offered up the category of directed symmetric pseudographs $\mathsf{SymGrph}$ as an interesting alternative to $\mathsf{rGrph}$. It is easy to see that a directed symmetric graph is basically the same thing as a simple graph. It just means that you have a directed graph, but for every directed edge, you have a directed edge going in the opposite direction. So you could basically just think of the two directed edges as one undirected edge.

I want to mention something else about the differences of the above categories. The crappiness of $\mathsf{rGrph}$ comes from it not allowing loops on vertices. We can be more precise with what this means. Given a functor $F: \mathcal{C} \to \mathbf{Set}$, a set[^1] of objects $(x_i \in \mathcal{C})_{i \in I}$ and a set of morphisms $(g_i : F(x_i) \to z)_{i \in I}$, a **final lifting** is a set $\overline{z}$ with $F(\overline{z}) = z$ such that for any $f : z \to F(e)$, the map $f$ lifts to a map $\overline{z} \to e$ if and only if each $(f \circ g_i) : F(x_i) \to F(e)$ lifts to a map $x_i \to e$. We say that $F$ is **topological** if it admits all final liftings.

The idea here is to generalize the good properties of the forgetful functor $U : \mathbf{Top} \to \mathbf{Set}$. The vague idea being that we can topologize any set with the discrete and indiscrete topology. In the above definition, we could have defined initial liftings and given a dual definition of co-topological, but a cool fact is that if a functor $F$ is topological iff it is co-topological. So we don't need to even worry about that.

FINISH

I had kind of hoped that we could just choose some category of graphs that we could stick to in all examples from computer science, but this is clearly not possible, simply because computer scientists, graph theorists and combinatorialists consider many different kinds of graphs, in some cases switching between them quite brazenly.

That being said, there is something interesting to be said about trying to find big categories which we can embed pretty much all examples of graphs into, and that is the category of directed pseudographs $\mathsf{dGrph}$.