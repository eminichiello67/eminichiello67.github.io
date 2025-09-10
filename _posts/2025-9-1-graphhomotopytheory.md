---
layout: post
title:  Papers on Graph Homotopy Theory
date:   September 1, 2025
description: A repository of papers
tags: graphs, homotopy theory
categories: math
---

Here we list some papers in the burgeoning subject of discrete homotopy theory, which considers applications of homotopy theory to discrete mathematics. The largest branch of this subject is graph homotopy theory, which itself splits into two sub-pieces: the $$\times$$-homotopy theory and the $$A$$-homotopy theory, which can be thought of as the simplicial graph homotopy theory and the cubical graph homotopy theory, respectively. This page will be updated occasionally

---

## A-Homotopy Theory
<details>
    <summary>(2001) <strong>Foundations of a Connectivity Theory for Simplicial Complexes</strong> by Hélène Barcelo, Xenia Kramer, Reinhard Laubenbacher and Christopher Weaver.</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Advances in Applied Mathematics 26, no. 2 (2001): 97–128. (<a href="https://doi.org/10.1006/aama.2000.0710">link</a>) <br></li>
    <li>I consider this to be the first paper in A-homotopy theory, even though it is based off of papers by Atkins and his students, inspired by work in the social sciences on social dynamics, which are about what he calls Q-analysis of simplicial complexes. In this paper, Barcelo et al really get to work putting Atkins' idea on a a rigorous footing.</li>
    <li>They define the A-homotopy group \(A^q_n(\Delta, x_0)\) of a simplicial complex.</li>
    <li>They associate to every simplicial complex \(\Delta\) a \(q\)-conectivity graph \(\Gamma^q(\Delta)\), whose vertices are the simplices of \(\Delta\) of dimension \(\geq q\) and whose edges connect those simplices which share a \(q\)-face. They define the \(A\)-homotopy groups of a graph \(A_n(G, x_0)\) such that \(A_n(\Gamma^q(\Delta), x_0) \cong A^q_n(\Delta, x_0)\).</li>
    <li>They show that the \(A\)-fundamental group \(A^q_1(\Delta, x_0) \) can be computed easily by taking the \(q\)-connectivity graph \(\Gamma^q(\Delta)\) and filling in all 3 and 4-cycles with a 2-cell, and taking the usual fundamental group of the resulting CW complex.</li>
    <li>They prove a Seifert-Van Kampen type theorem for the \(A\)-fundamental group.</li>
</ul>
</details>

<details>
    <summary> (2005) <strong>Perspectives on A-Homotopy Theory and Its Applications</strong> by Hélène Barcelo, and Reinhard Laubenbacher.
   </summary>
   <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
   <li>Discrete Mathematics, Formal Power Series and Algebraic Combinatorics 2002 (FPSAC’02), vol. 298, no. 1 (2005): 39–61. (<a href="https://doi.org/10.1016/j.disc.2004.03.016.">link</a>) </li>
   <li> Really wonderful paper that gives a whole bunch of applications and relationships of \(A\)-homotopy theory to combinatorics. Barcelo and Laubenbacher show that \(A\)-homotopy theory shows up in the work of several combinatorialists:
       <ul>
          <li>in the <a href="https://doi.org/10.1016/0095-8956(73)90005-1">work of Maurer (1973)</a> on matroids. In particular Maurer proves that if \(M\) is a matroid, and \(\mathcal{B}(M) \) is the basis graph of \(M\), then \(\mathcal{B}(M)\) has \(A_1(\mathcal{B}(M) = 0 \).</li>
          <li>in the <a href="https://doi.org/10.1007/BF01896190">work of Lovasz (1977)</a> on \(k\)-fold partitions of \(k\)-connected graphs,</li>
          <li>in the <a href="https://web.math.pmf.unizg.hr/glasnik/18.1/18101.pdf">work of Malle (1983)</a>, who proves that if \(G\) is a graph, then \(A_1(G) = 0\) if and only if every cycle in \(G\) has a pseudoplanar net in \(G\).</li>
          <li> in the work of Babson and Bjorner, but published later by <a href="">Barcelo-Severs-White (2011)</a> as Theorem 3.1. The \(k\)-equal arrangement, \(A_{n,k} \) is the collection
          of all subspaces of \( \mathbb{R}^{n+1} \) given by \(x_{i_1} = x_{i_2} = \dots = x_{i_k}\)
          over all indices \({i_1, \dots , i_k} \subseteq [ n + 1]\), with the relation \(\sum_{i=1}^{n+1} x_i = 0 \). They prove that if \(U(A_{n,k}) \) denotes the complement of \(A_{n,k}\) in \(\mathbb{R}^{n+1} \), then \(\pi_1(U(A_{n,k})) \cong A_1^{n - k + 1}(\Delta(B_n)) \), where \(\Delta(B_n) \) is the order complex of the Boolean lattice \(B_n = \{0,1\}^n \). </li>
       </ul>
   </li>
</ul>
</details>

<details>
    <summary>(2006) <strong>Homotopy Theory of Graphs</strong> by Eric Babson, Hélène Barcelo, Mark Longueville, and Reinhard Laubenbacher.</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>J. Algebraic Comb. 24, no. 1 (2006): 31–44. (<a href="https://doi.org/10.1007/s10801-006-9100-0">link</a>)</li>
    <li>One of the key results of the 2001 Foundations paper computes the \(A\)-fundamental group of a graph \(G\) in terms of the usual fundamental group of a related space \(X_G \) obtained by filling in the 3 and 4 cycles with 2-cells. This paper addresses the question of this can be achieved for the higher \(A\)-homotopy groups. </li>
    <li> They define the loop graph \(\Omega G \) of a graph \(G \) and prove that \( A_{n+1}(G) \cong A_n(\Omega G) \) for \(n \geq 0 \).</li>
    <li> Given a graph \(G \), they construct a cubical set \(N_1(G) \) (which they denote \(M_*(G) \), but we will use the notation from <a href="https://doi.org/10.1112/S0010437X24007486.">Kapulkin-Carranza (2024)</a>) and prove that if a certain cubical approximation conjecture holds (and note that as of this writing, this conjecture is still open) then \(\pi_n(N_1(G)) \cong A_n(G) \) for all \(n \geq 1 \).
    <ul>
        <li>Note that the above result was later proven in <a href="https://doi.org/10.1112/S0010437X24007486.">Kapulkin-Carranza (2024)</a>, using abstract homotopy theory, entirely avoiding having to prove the cubical approximation conjecture.</li>
    </ul>
    </li>
</ul>
</details>

<details>
    <summary>(2014) <strong> Discrete Homology Theory for Metric Spaces</strong> by Hélène Barcelo, Valerio Capraro, and Jacob A. White.
    </summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Bulletin of the London Mathematical Society 46, no. 5: 889–905. (<a href="https://doi.org/10.1112/blms/bdu043">link</a>) </li>
    <li>Develops a notion of discrete homology for metric spaces that satisfies a discrete form of the Eilenberg-Steenrod axioms.</li>
</ul>
</details>

<details>
    <summary>(2019) <strong>Discrete Cubical and Path Homologies of Graphs</strong> by Hélène Barcelo, Curtis Greene, Abdul Salam Jarrah, and Volkmar Welker.</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Algebraic Combinatorics 2, no. 3 (2019): 417–37. (<a href="https://doi.org/10.5802/alco.49">link</a>) </li>
    <li>Specializes the definition of discrete homology for metric spaces from <a href="https://doi.org/10.1112/blms/bdu043">Barcelo-Capraro-White (2014)</a> to graphs, calls it discrete cubical homology. We will use the notation \(H_n^\square(G) \) for these homology groups of a graph \(G \).</li>
    <li>Proves that all trees are \(A\)-contractible</li>
    <li>Proves that all hypercubes \(Q_n\) are \(A\)-contractible</li>
    <li>Proves that all chordal graphs are cubical acyclic, i.e. if \(G\) is chordal, then \(H_n^\square(G) = 0 \) for all \(n \geq 1\).</li>
    <li>Proves that complete bipartite graphs are cubical acyclic</li>
    <li>Proves that discrete cubical homology and path homology do not always agree. Also shows that the Greene Sphere graph has nontrivial \(H_2^\square\) (Theorem 6.1).</li>
</ul>
</details>

<details>
    <summary>(2020) <strong>Higher Discrete Homotopy Groups of Graphs</strong> by Bob Lutz.</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li> Algebraic Combinatorics 4, no. 1 (2021): 69–88.
(<a href="https://doi.org/10.5802/alco.151.">link</a>) </li>
</ul>
</details>



<details>
    <summary>(2021) <strong>On the Vanishing of Discrete Singular Cubical Homology for Graphs</strong> by Hélène Barcelo, Curtis Greene, Abdul Salam Jarrah, and Volkmar Welker.</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>SIAM Journal on Discrete Mathematics, 2021 (<a href="https://epubs.siam.org/doi/abs/10.1137/20M1338484">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2024) <strong>Cubical Setting for Discrete Homotopy Theory, Revisited</strong> by Krysztof Kapulkin and Daniel Carranza</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Compositio Mathematica 160, no. 12 (2024): 2856–903.
(<a href="https://doi.org/10.1112/S0010437X24007486.">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2025) <strong>The Fundamental Group in Discrete Homotopy Theory</strong> by Krysztof Kapulkin and Udit Mavinkurve</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Advances in Applied Mathematics 164 (March 2025): 102838 (<a href="https://doi.org/10.1016/j.aam.2024.102838.">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2025) <strong>The Lifting Properties of A-Homotopy Theory</strong> by Rachel Morrill</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>arXiv (<a href="https://doi.org/10.48550/arXiv.1904.12065">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2025) <strong>Mapping Fiber, Loop and Suspension Graphs in Naive Discrete Homotopy Theory</strong> by Rachel Morrill</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>arXiv (<a href="https://doi.org/10.48550/arXiv.2402.15714">link</a>) </li>
</ul>
</details>

---

## X-Homotopy Theory

<details>
    <summary>(2009) <strong>Hom complexes and homotopy theory in the category of graphs </strong> by Anton Dochtermann</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>European Journal of Combinatorics 30.2 (2009): 490-509 (<a href="https://doi.org/10.1016/j.ejc.2008.04.009">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2009) <strong>Homotopy groups of Hom complexes of graphs</strong> by Anton Dochtermann</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>	Journal of Combinatorial Theory, Series A 116.1 (2009): 180-194. (<a href="https://doi.org/10.1016/j.jcta.2008.06.001">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2017) <strong>Box Complexes and Homotopy Theory of Graphs</strong> by Takahiro Matsushita</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>Homology, Homotopy and Applications, vol. 19(2), 2017, pp.175–197 (<a href="http://dx.doi.org/10.4310/HHA.2017.v19.n2.a10">link</a>) </li>
</ul>
</details>

<details>
    <summary>(2025) <strong>Thomason-Type Model Structures on Simplicial Complexes and Graphs</strong> by Emilio Minichiello</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>arXiv (<a href="https://arxiv.org/abs/2508.08195">link</a>) </li>
</ul>
</details>

---

## Čech Closure Spaces and Pseudotopological Spaces

<details>
    <summary>(2021) <strong>Eilenberg-Steenrod homology and cohomology theories for Čech's closure spaces</strong> by Peter Bubenik and Nikola Milićevic</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>arXiv (<a href="https://arxiv.org/abs/2112.13421">link</a>) </li>
</ul>
</details>


<details>
    <summary>(2021) <strong>Homotopy, homology, and persistent homology using closure spaces</strong> by Peter Bubenik and Nikola Milićevic</summary>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

<ul>
    <li>	J. Appl. Comput. Topol. 8 (2024), no. 3, 579-641 (<a href="https://doi.org/10.1007/s41468-024-00183-8">link</a>) </li>
</ul>
</details>
