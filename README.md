Django Task - "clauselocator"
=================

Core to Robin AI's product is the ability to replace clauses within original client documents, with more suitable replacement clauses.

We require the ability to locate a sentence within a paragraph.

The task concerns the design and implementation of an API Endpoint, whose inputs are a sentence and paragraph. The response from the API should contain the start and end character indexes of the sentence within the paragraph, where they can be found.

1. Design the API Endpoint. This should include the resource name, request and response content, and appropriate response codes.  
2. Implement the API Endpoint using Django and any libraries you deem appropriate. The endpoint should handle the following cases:
    a. Where the whole sentence is contained within the paragraph
    b. Where the end of the sentence is contained within the paragraph
    c. Where the start of the sentence is contained within the paragraph 

Don't worry if you do not finish implementing all of the functionailty in 30 minutes - the quality of the code you write is more important than whether the task has been completed.

Examples:
1. Paragraph Text: "This is a legal document. You agree to hold and treat data in the strictest of confidence. If you are in agreement, please sign."
Sentence Text: "You agree to hold and treat data in the strictest of confidence."
In this example, the **start index** is **26**, and the **end index** is **89**.

2. Paragraph Text: "If you are in agreement, please return the signed document. You will then be bound to the agreement."
Sentence Text: "If you are in agreement, please return the signed document."
In this example the **start index** is **0**, and the **end index** is **58**.
