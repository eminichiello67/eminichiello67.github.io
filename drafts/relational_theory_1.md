---
layout: post
title:  Introduction to Relational Theory
date:  N/A 
description: The inaugural post! What is a diffeological space?
tags: diffeological_spaces
categories: math
---

In this post, we will cover the relational theory of databases. This will help us set the stage for comparison with categorical database theory later on in the series.

**Rem:** In what follows, we fix a countably infinite set $\mathsf{Dom}$, called the **domain**, whose elements $c \in \mathsf{Dom}$ we call **constants**. There will be much to say about the domain later. 

We also note that everything we present in what follows is known as the **unnamed relational formalism**. There is an alternative **named relational formalism**, which requires a set of attributes. These are different frameworks that are ultimately equivalent. There are pros and cons to both formalisms: the unnamed formalism is mathematically simpler and closer to traditional model theory, which is why I chose it for this post, but the named formalism allows for the definition of a natural join operation, and tends to be used more by database theorists.

**Def:** A **relational database schema** consists of a set $\mathbf{R}$, whose elements we call **relation symbols**, along with a function $\text{ar}: \mathbf{R} \to \mathbb{N}$ called the **arity function**. If $R \in \mathbf{R}$, and $\text{ar}(R) = n$, then we say that $R$ has **arity** $n$.