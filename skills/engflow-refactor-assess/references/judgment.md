# Refactoring judgment examples

Use evidence and net benefit, not a fixed list of smells or a complexity threshold.

## Worthwhile consolidation

Three call sites implement the same authorization rule. Inspected history and code
show two recent rule changes missed one site. A shared policy function with explicit
inputs can remove the demonstrated divergence risk. Explain behavior parity, dynamic
or external consumers, migration cost and focused checks. Recommend only the smallest
shared contract that solves that burden; assessment still does not authorize edits.

## Preference without demonstrated benefit

A long but linear parser follows the grammar closely. Splitting each branch into a
one-line helper adds navigation without removing duplication or isolating independent
responsibility. Function length or a preferred style alone is insufficient evidence;
recommend no refactor unless a concrete maintenance problem emerges.

A correctness defect in a proposed patch belongs in code review. Do not expand that
finding into an unrelated architecture rewrite, or call a changed public behavior a
behavior-preserving refactor.
