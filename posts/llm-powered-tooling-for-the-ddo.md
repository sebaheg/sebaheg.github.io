---
title: The LLM-powered data stack
date: 2026-01-07
description: My first blog post
publish: false
---
It seems to me that there are two camps of people right now, those who have seen the light of LLM-powered coding tools and those that haven't. As a product-person, I just got to spent some time during the winter holiday to try out tools like Cursor and Claude Code and that was definitively a precondition for me to see it, but I don't think that's the only thing. It seems like there is a lot of people out there using Cursor on a daily basis and saying "yeah, it's nice for tab-completion and refactoring". In addition to first-hand usage, it's about extrapolating the consequences. 

There is not a lack of blog posts and books on the topic of data-driven organisations (DDO). But in a world where the code is writing itself, I think some updates to our old frameworks and mental models are due. I'll implicitly focus on what I know best in this post - data work, especially, data science in vertical industries. 

from the perspective of product-development

### The promise of the data-driven organisation
The idea of a data-driven organisation is as old as... 

### The key components of the LLM-powered data stack
My bet is that the best tooling for data teams will take the following form factor, in order, from the ground up: 

1) Vendor-maintained, code-first intrastructure primitives
2) Opinionated, domain specific data models and tools
3) Prompt-to-X (pipeline, dashboard, app, test, etc)
4) Visual, extensive test- and validations

Let's unpack this. 

### Vendor-maintained, code-first intrastructure primitives and data tools
These are the infrastructure, API and visualisation lego bricks. Data teams should focus on business outcomes and not on reinventing building blocks that could be purchased from vendors specialised on just this. Code-first tools enables a flexibility and precision, no-code tools will never be able to meet. But code-first goes deeper than that, it's tools that expose full transparancy and control to the user. Here is an example of an error message I ran into in a cloud app deployment platform: 

```bash
Build failed due to eceeded memory. Please contact support for more information. 
```

I had no clue what machine I was using for the deployment, nor any logs that could help me debug. Not to speak of the control That I would need to change the deployment specs and fix the problem. 

You might say: "if code is for free, why don't I just build my own primitives?". Well, even in a world where code is for free, every line of code adds to your technical debt. And when the code breaks, you can yell at Claude all day long, but the responsibility is still with you. If it's not core to your business your better of passing that headache on to someone else. 

### Opinionated, domain specific data models and tools
Data teams inside of companies develop data products, like APIs, models, dashboards, to solve specific business problems. The degrees-of-freedom for creating these products is endless. Being opinionated means, knowing the problem and the user so well that you can articulate the *how* of the solution better than anyone else. The user gets surprised with delight of the problem framing and recognition. That's the definition of [product taste](https://www.linkedin.com/pulse/taste-sarah-guo-u9qcf/). 

### Prompt-to-X (pipeline, dashboard, app, test, etc)
The entry point data stack is most likely 


### Visual test, observability and validation 
Given that we are delagating more and more of writing code to LLMs, we need other ways to build up confidence than direct code interaction. The way to do this is testing and observing code execution in safe environments before deploying. I think this will take the form of intuitive UIs that lets you sift through the result of 1000s LLM- and developer-written tests quickly. 

GPT-wrapper:
The assumption is that there is a value in knowing more than the customer about a particular thing. You prompt it in a smarter way and provide a better UI. 

The toolkit for data scientists is increasingly just pen and paper or the whiteboard. 