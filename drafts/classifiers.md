Something that has bugged me for my whole PhD has been an understanding of the Giraud axioms, especially in the context of infinity topoi.

This led me to try to understand object classifiers. Classifiers come up all the time in bundle theory, but Cisinski's book really helped me understand the Grothendieck construction and how its related to topos theory.

You can classify propositions (sets that are either a singleton or empty) in Sets, you can classify sets in Gpd, you can classify Gpd in 2Gpd, etc. (Joachim Kock has beautiful explanation in epi/mono classifier zulip discussion). 

But the Grothendieck construction seems really close to a classifier statement. That is because it is. Cisinski shows that the object classifier for sSet is U_* -> U, which is weird to describe. U is a simplicial set where U_n is the set of morphisms X -> Delta^n along with choices of pullback for every map Delta^m -> Delta^n. See if I can understand that better. This classifies all morphisms X -> Y, and that morphism is a fibration iff Y -> U factors through S, which is the subsimplicial set of U of maps X -> Delta^n that are fibrations. Thus the Grothendieck construction is a special case of object/morphism classification.