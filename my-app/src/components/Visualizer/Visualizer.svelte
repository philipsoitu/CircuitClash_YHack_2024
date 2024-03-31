<script lang="ts">
	import { string } from 'zod';
	import Canvas from './Canvas.svelte';
	export let width: number;
	export let height: number;
	export let shdl: string;

	let possibleViewers: string[] = ['main'];
	let currentViewer: number = 0;
	function generatePossibleViewers() {}
</script>

<div>
	{#each possibleViewers as possibleViewer, i}
		<button>{possibleViewers[i]}</button>
	{/each}
</div>
<Canvas {width} {height} {shdl} />
