# Azure_AI_P-S-10

To complete the lab task you outlined, follow these key steps. Here's a quick guide summarizing the process:

### 1. **Azure Setup**

- **Sign in** to [Azure Portal](https://portal.azure.com) using the provided credentials:
- **Create an Azure OpenAI Resource**:
  - Go to **ResourceGroup**.
  - Choose a **Region**: 
  - Name your resource with a **unique name** and select the pricing tier.

### 2. **Deploy the Model**

- In the Azure portal, navigate to the deployed Azure OpenAI resource.
- Access the **AI Foundry portal** from the resource's Overview page.
- Deploy the model:
  - **Deployment name**: Choose a unique name.
  - **Model version**: 
  - Set **Rate Limit**:

### 3. **Prompt Engineering**

- In the **Chat Playground**:
  -Set different system messages and test with differnet prompts.
  -Example:
  - Set the initial system message to: `You are an AI assistant that helps people find information.`
  - Submit the article classification prompt with the **drought scenario**.
  - And observ the output

### 4. **Prepare App in Visual Studio Code**

- **Clone the GitHub Repository**:
  - Open **Visual Studio Code**.
  - Clone `https://github.com/MicrosoftLearning/mslearn-openai`.
  - Open the cloned folder in VS Code.
- **Install Azure OpenAI SDK**:
  - Open a terminal in the relevant language folder:
    - For **Python**: `pip install openai==1.13.3`
- **Configure App**:
  - Update the configuration file:
    - For **Python**: Edit `.env`.
  - Add the **endpoint**, **key**, and **deployment name** from Azure.

### 5. **Run and Test the App**

- Modify the `system.txt` file with the required system messages for each task.
- Run the app:

