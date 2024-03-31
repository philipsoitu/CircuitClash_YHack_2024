<script lang="ts">
	// @ts-ignore
	import { SignIn, SignOut } from '@auth/sveltekit/components';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	export let data;
	let currentnum = 1
	console.log(data.level.levelnumber)
</script>


	{#if data.user}
	<main class="flex justify-between rounded-2xl border-2 main px-4 py-2">
		<div class="grid flex-1 gap-2 overflow-hidden lg:grid-cols-4 m-8">
			{#each data.questions as question, index (question.id)}
				{#if data.level.levelnumber == index + 1} 
					<div class="card flex flex-col items-center justify-items-center gap-4">
					<h1 class="h1 -mb-1">Question {question.id}</h1>
					<h2 class="">{question.name}</h2>
					<a class="btn btn-sm" href="/circuit">Try now</a>
					</div>
				{:else}
					<div class="card flex flex-col items-center justify-items-center gap-4" style="opacity: 0.5; background-color: #333; pointer-events: none;">
					<h1 class="h1 -mb-1" style="color: darkgrey;">Question {question.id}</h1>
					<h2 class="" style="color: darkgrey;">{question.name}</h2>
					<a class="btn btn-sm" style="background-color: #555;" href="/circuit">Try now</a>
					</div>
				{/if}
			{/each}
			
		
		</div>
	</main>
	{:else}
	<div class="mx-auto my-auto card items-center sign-in-box">
		<h1 class="h1 mt-2">You are not signed in</h1>
		<SignIn>
			<div slot="submitButton" class="btn mb-2">Sign in</div>
		</SignIn>

	</div>
	{/if}

	

