<script lang="ts">
	// @ts-ignore
	import { SignIn, SignOut } from '@auth/sveltekit/components';
	import { page } from '$app/stores';
	export let data;
	
</script>

<main class="container flex flex-1 flex-col overflow-hidden ">
	{#if data.user}

		<div class="grid flex-1 gap-2 overflow-hidden lg:grid-cols-4 m-8">
			{#each data.questions as questions}
				<div class="card flex flex-col items-center justify-items-center gap-4">
					<h1 class="h1 -mb-1">Question {questions.id}</h1>
					<h2 class="">{questions.name}</h2>
					<button class="btn">Try it out</button>
				</div>

			{/each}
			

		</div>
	{:else}
	<div class="mx-auto my-auto card items-center">
		<h1 class="h1">You are not signed in</h1>
		<SignIn>
			<div slot="submitButton" class="btn">Sign in</div>
		</SignIn>

	</div>
	{/if}

	
</main>
