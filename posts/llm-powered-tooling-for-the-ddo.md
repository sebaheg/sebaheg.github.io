---
title: The AI-powered data stack
date: 2026-01-07
description: My first blog post
publish: false
---
It’s probably an understatement to say that software development sits at an inflexion point in beginning of 2026. It’s no longer just about tab completion and code assistants; AI code agents like Claude Code are autonomously producing full PRs that are merged into production-grade codebases. It is undeniably looking like the code of the future will - to a large extent - write itself. It’s a strange type of intelligence that, in one stroke, creates some impressive piece of code or math, just to face plant by confidently miscounting the number of r’s in “strawberry” or miscalculating a simple addition. What will all of this mean for in-house data teams and the data stack they use? That’s what I want to take a stab at here. 

The goal of an in-house data team is to drive business value (measurable or not) by enabling automated processes and better decisions (often under uncertainty), ultimately creating data-driven organisations. Data-driven organisations live on some sort of scale between zero and 100%, where later percentage points become increasingly expensive to achieve. At one end, you have legacy businesses and on the other, digital- and AI-native ones. Also, inside the organisation, you might have very different degrees of “data-drivenness”.

### Vibe coding vs AI-assisted coding
It’s probably first a good idea to establish some definitions here. Vibe coding is about prompting and AI to code, without even looking at what is going on behind the scenes. AI-assisted coding is about using AI code generation while still ensuring sound architectural decisions and overall code quality and reliability. They both have their place in different situations, but in general, the higher the complexity and consequences of software failure, the more you want to err on the side of AI-assisted coding. 

### “The one step forward, two steps back”-problem
As most vibe coders out there can testify, building software with AI can be a pain in the ass. You manage to build some sort of prototype app, but then when you want to add some additional functionality, you simultaneously break the functionality of two unrelated features. As you took one step forward, the AI threw you two steps back. The underlying problem here is that all software lives in some context and assumes user intent; if the AI gets this wrong, it will easily tangle up things in your codebase. Throw more AI on the problem, and it will just amplify the mess it has created. 

### LEGO bricks to the rescue
The solution to this problem is constraining your AI with well-grounded and sound guardrails. You create maintainable, reusable building blocks - like LEGO bricks - that the AI can use to stitch things together, rather than building everything from the ground up on incomplete context and assumptions. Your job as a programmer is to ensure the AI serves the right context and intent by continuously factoring out modular pieces of the code as standalone building blocks. In a way, coding with AI is like climbing; each extracted building block is like a bolt in the rock - it locks in your progress and enables you to climb even further. 

### The key components of the AI-powered data stack
My bet is that the best tooling for data teams will take the following form factor, in order, from the ground up: 

1) Transparent and controllable cloud infrastructure primitives
2) Opinionated, domain-specific data models and tools
3) Prompt-to-X (pipeline, dashboard, app, test, etc.)
4) Visual, extensive test- and validations

Let's unpack this. 
