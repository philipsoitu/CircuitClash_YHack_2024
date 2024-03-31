<!-- ChatAssistant.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Configuration from 'openai';
  import  OpenAIApi  from 'openai';

  // For browser-based environments
  import { browser } from '$app/environment';

  let inputValue: string = '';
  let messages: { role: 'user' | 'assistant'; content: string }[] = [];
  let loading = false;

  const configuration = new Configuration({
    apiKey: 'YOUR_API_KEY',
  });

  // Use the browser's built-in fetch function for client-side rendering
  const openai = new OpenAIApi(configuration, browser ? undefined : undefined);

  // For server-side rendering (SSR) or Node.js environments
  if (!browser) {
    import('node-fetch').then(({ default: fetch }) => {
      openai.configuration.fetchImpl = fetch;
    });
  }

  onMount(() => {
    messages = [
      {
        role: 'assistant',
        content: 'Hello! I am an AI assistant. How can I help you today?',
      },
    ];
  });

  async function handleSubmit() {
    // ... (the rest of the code remains the same)
  }
</script>

<!-- ... (the rest of the component remains the same) -->