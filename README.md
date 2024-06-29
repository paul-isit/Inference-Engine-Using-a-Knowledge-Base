# Inference-Engine-Using-a-Knowledge-Base
This project aims to implement an inference engine that uses a knowledge base to infer if a sentence is entailed by the given knowledge base.

The inference engine makes use of three algorithms, namely Truth Table (TT), Forward Chaining (FC) and Backward Chaining (BC), to make its deductions. Truth table algorithm can work with all types of knowledge bases but FC and BC algorithms work with Horn-Form KBs. 
But this project incorporates knowledge bases with general propositional sentences as well. This is because each sentence that we "tell" the knowledge base is first converted to Conjunctive Normal Form (CNF) and then to a Horn sentence, for consistency sake.

We use a simple text file format to "TELL" the KB all the sentences and "ASK" the KB the query that we want to know if it can be entailed by the given KB.
<img width="513" alt="Screenshot 2024-06-29 at 2 11 52 PM" src="https://github.com/paul-isit/Inference-Engine-Using-a-Knowledge-Base/assets/146925111/07d0ae88-c437-49e0-ad9a-30bf61bf8249">


USE INSTRUCTIONS are provided in the report but here is a screenshot of it
<img width="810" alt="Screenshot 2024-06-29 at 1 49 28 PM" src="https://github.com/paul-isit/Inference-Engine-Using-a-Knowledge-Base/assets/146925111/054f4270-9e47-404c-8599-71ccd80c25a6">

The output provided by any of the algorithms is a YES or a NO as in if the KB entails the query or not. Moreover, TT provides the number of models that satisfy the query from the given KB and FC and BC provide all the symbols entailed in the entailment order to prove that the given KB is sufficient to entail query.
<img width="538" alt="Screenshot 2024-06-29 at 2 14 31 PM" src="https://github.com/paul-isit/Inference-Engine-Using-a-Knowledge-Base/assets/146925111/92086792-256d-47ef-91b0-8b1e0869effe">

