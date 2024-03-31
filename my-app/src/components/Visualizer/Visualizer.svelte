<script lang="ts">
	import { string } from 'zod';
	import Canvas from './Canvas.svelte';
	export let width: number;
	export let height: number;
	export let shdl: string;

	let possibleViewers: string[];
	let currentViewer: string;
	function generatePossibleViewers() {}
</script>

<div>
	{#each possibleViewers as possibleViewer, i}
		<button
			aria-current={selected === color}
			aria-label={color}
			style="background: {color}"
			on:click={() => (selected = color)}>{i + 1}</button
		>
	{/each}
</div>
<Canvas {width} {height} {shdl} />
