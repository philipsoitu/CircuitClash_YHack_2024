<script lang="ts">
	import '../main.css';
	export let data;
	import { QuestionMark } from 'tabler-icons-svelte';
	// @ts-ignore

	import { SignOut } from '@auth/sveltekit/components';

	import { popup, type PopupOptions } from '$lib/popup';

	const popupSettings: PopupOptions = {
		popupId: 'popupNavIcon',
		placement: 'bottom'
	};
</script>

<div
	class="sticky inset-2 z-50 m-2 flex justify-between rounded-lg border-2 border-dark bg-white px-4 py-2"
>
	<a class="flex items-center gap-2" href="/">
		<h1 class="h1">Circuit</h1>
	</a>

	<div class="flex items-center gap-4">
		<a class="btn btn-sm" href="/docs"> Docs </a>

		{#if data.user}
			<button class="btn btn-flat h-10 w-10 p-0" use:popup={popupSettings}>
                <img src={data.avatar} class="object-cover" alt="your user avatar" />
            </button>
		{:else}
			<div class="btn btn-flat h-10 w-10 p-0">
				<QuestionMark />
			</div>
		{/if}
	</div>
</div>

<div class="popup" id={popupSettings.popupId}>
	<div class="popup-arrow" id="arrow" />

	<div class="card flex w-40 flex-col items-stretch bg-background py-2">
		<SignOut>
			<div slot="submitButton" class="">Sign out</div>
		</SignOut>
	</div>
		
	
</div>

<slot />
