---
title: The AI-powered data stack
date: 2026-01-10
description: My first blog post
publish: true
---
It’s probably an understatement to say that software development sits at an inflection point at beginning of 2026. It’s no longer just about tab completion and code assistants; AI code agents like Claude Code are autonomously producing full PRs that are merged into production-grade codebases. It is undeniably looking like the code of the future will - to a large extent - write itself. It’s a strange type of intelligence that, in one stroke, creates some impressive piece of code or math, just to face plant by confidently miscounting the number of r’s in “strawberry” or miscalculating a simple addition. What will all of this mean for in-house data teams and the data stack they use? That’s what I want to take a stab at here. 

The goal of an in-house data team is to drive business value (measurable or not) by enabling automated processes and better decisions (often under uncertainty), ultimately creating data-driven organisations. Data-driven organisations live on some sort of scale between zero and 100%, where later percentage points become increasingly expensive to achieve. At one end, you have legacy businesses and on the other, digital- and AI-native ones. Also, inside the organisation, you might have very different degrees of “data-drivenness”.

### Vibe coding vs AI-assisted coding
It’s probably first a good idea to establish some definitions here. Vibe coding is about prompting an AI to code, without even looking at what is going on behind the scenes. AI-assisted coding is about using AI code generation while still ensuring sound architectural decisions and overall code quality and reliability. They both have their place in different situations, but in general, the higher the complexity and consequences of software failure, the more you want to err on the side of AI-assisted coding. 

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

#### Transparent and controllable cloud infrastructure primitives
Deploying code on cloud infrastructure can be tedious, especially when iteration loops are long. This is an area where AI code agents work surprisingly well. They read documentation, analyse deployment logs at speeds far beyond what’s humanly possible. For this to work, the cloud infrastructure should provide logs in a code-queryable way and enable dialing ling the infrastructure knobs to fix deployment issues. 

Here is an example of an error message I ran into in a cloud app deployment platform the other day: 

```
Build failed due to exceeding memory. Please contact support for more information. 
```

Compare this to the deployment logs you get from a tool like [Modal](https://modal.com/):

```
=> Building image for Function: my_function
   Collecting pandas==2.1.0 (from -r /requirements.txt (line 3))
   Successfully installed numpy-1.26.0 pandas-2.1.0
=> Image built successfully in 12.3s
=> Deploying function my_function to region us-east-1
   Memory: 2048MB | CPU: 2.0 | Timeout: 300s
=> Function deployed: https://my-app--my_function.modal.run
```

This is like candy for your AI code agent.


#### Opinionated, domain-specific data models and tools
Inhouse data teams develop data products, like APIs, models, and dashboards, to solve specific business problems. The degrees-of-freedom for creating these products are endless. Being opinionated means knowing the problem and the user so well that you can articulate the *how* of the solution better than anyone else. The user gets surprised with the delight of the problem framing and recognition. That, for me, is the definition of [product taste](https://www.linkedin.com/pulse/taste-sarah-guo-u9qcf/). 

#### Prompt-to-X (pipeline, dashboard, app, test, etc)
Now with the right building blocks in place, what is left is quickly producing the right glue code and customisations to the aforementioned data products. Technical or non-technical users prompt what they want to achieve and the AI code agent composes data products with well-defined and documented blocks. Being built using sound and trusted foundations, these data products will be significantly more reliable and easier to maintain - both for coders and for the AI code agent itself. 

#### Visual test, observability and validation 
Given that we are delegating more and more of writing code to AI code agents, we need other ways to build up confidence than direct code interaction. The way to do this is to test and observe code execution in safe environments before deploying, and then constantly validate code that is in production. This will take the form of visual, intuitive UIs that let you sift through the result of thousands of AI- and developer-written tests quickly. Here the developer should have a way to at least validate the most important tests and perform a sanity check before hitting “deploy”. 

### On responsibility
You might say: "if the code writes itself, why don't I just let the AI code agent build my own building blocks as well?". Well, even in a world where the code writes itself, every single line of code adds to your accumulated technical debt. When a vendor-maintained building block breaks, you can call them up and have them fix it. If the code of your AI code agent breaks, you can yell at it all day, but you are still on the hook for making things work. If it's not core functionality or knowledge to your business you're better off passing that headache on to someone else. 

### Pens and whiteboards
With this new data stack in place, data teams will be increasingly climb the ladder of abstraction from the *how* to implement to the *what* to implement. Deciding what to do, deciding on and implementing on the right workflows and collaboration models in the team. The work of a data team is increasingly going to happen on the human-level of communication and context sharing, and some of the most important tools for that are pens and whiteboards. That is not to say that analytical thinking is not needed anymore. There is [evidence](https://www.pnas.org/doi/10.1073/pnas.1603205113) that learning math alters how your brain works, and will be instrumental to your effectiveness using AI tools. 

### Will Python die? 
[Some think](https://matthewrocklin.com/ai-zealotry/) that Python over time will die out. Python was built on the importance of fast code iteration and readability. As the code writes itself and is read less, these assumptions are no longer true, the argument goes. So why not just build your stack with Rust and Typscript instead? This is maybe true for highly senior developers and teams building software products, where performance really matters. But that's not the case for most data teams, where performance is not the main constraint and the benefits of readable code for understanding and last-mile human implementations will still be very high. 

Outro... 