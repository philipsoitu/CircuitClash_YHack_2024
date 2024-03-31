<script lang="ts">

	import CodeMirror from 'svelte-codemirror-editor';
	import { oneDark } from '@codemirror/theme-one-dark';
	import Visualizer from '../../components/Visualizer.svelte';
	import SuperDebug from 'sveltekit-superforms';
	import { onMount } from 'svelte';
	import TruthTable from './tablegenerate.svelte'
	let buttontext = ["Show Question","Show circuit"]
	let buttontextindex = 0
	let description = 'Define the functionality of a full 1-bit adder in shdl.'
	export let data;
	let title = 'Full 1-bit Adder'
	let qnum = 1;
	let inputData = ['I01', 'I02'];
	let outputData = ['O01', 'O02'];
	let truthTable = [
		{'I01': 0, 'I02': 0, 'O01': 0, 'O02': 0},
		{'I01': 0, 'I02': 1, 'O01': 1, 'O02': 0},
		{'I01': 1, 'I02': 0, 'O01': 1, 'O02': 0},
		{'I01': 1, 'I02': 1, 'O01': 0, 'O02': 1}
	];
	let value = '';
	function changeText() {
		if (buttontextindex === 0){
			buttontextindex = 1
		}
		else{
			buttontextindex = 0
		}
	}
</script>


<main class="container flex flex-1 flex-col overflow-hidden ">
	<div class="grid flex-1 gap-2 overflow-hidden lg:grid-cols-2">
		{#if buttontextindex===1}

			<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
					<div class="card">
						<h1 class="h1">Q{data.messages[0].id}: {data.messages[0].name}</h1>
						<p class="questiondesc">{data.messages[0].description}</p>
						<TruthTable {inputData} {outputData} {truthTable} />				</div>

			</div>
		{:else}
		<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
			<div class="card">
				<h1 class="h1">Circuit:</h1>
				<Visualizer width={500} height = {500} shdl= {value}/>
			</div>

	</div>

		{/if}


		<div class="col-span-1 my-4 hidden rounded-xl bg-primary p-4 lg:grid overflow-y-auto">
			<CodeMirror
				bind:value
				styles={{
					'&': {
						width: '100%',
						maxWidth: '100%',
						height: '33em'
						
					}
				}}
				theme={oneDark}
				placeholder={'Start coding here..'}
			/>
			<button class="btn mt-4" on:click={changeText}>{buttontext[buttontextindex]}</button>
		</div>
	</div>
</main>
