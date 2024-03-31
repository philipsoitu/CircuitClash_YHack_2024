<script lang="ts">
	import Canvas from './Canvas.svelte';
	export let width: number;
	export let height: number;
	export let shdl: string;

	let possibleViewers: string[] = ['main'];
	
	function generatePossibleViewers(inputString: string) {
		// Regular expression to match STARTGATE and ENDGATE blocks along with their contents
		const gateRegex = /STARTGATE.*?ENDGATE/gms;

		// Extracting all occurrences of STARTGATE and ENDGATE blocks
		const gates = inputString.match(gateRegex) || [];

		// Removing the STARTGATE and ENDGATE blocks from the input string
		const trimmedString = inputString.replace(gateRegex, '');

		// Extracting individual lines from the trimmed string
		const lines = trimmedString
			.split('\n')
			.map((line) => line.trim())
			.filter((line) => line !== '');

		// const result = [...lines].join('\n');
		const wordFollowingStartgateRegex = /STARTGATE\s+(\w+)/g;

		// Array to collect all matches
		const wordsFollowingStartgate = [];
		wordsFollowingStartgate.push('MAIN');
		// Finding and storing all matches
		let match = [];
		while ((match = wordFollowingStartgateRegex.exec(inputString)) !== null) {
			wordsFollowingStartgate.push(match[1]);
		}
		return wordsFollowingStartgate;
	}

	function parseText(inputString: string) {
		// Regular expression to match STARTGATE and ENDGATE blocks along with their contents
		const gateRegex = /STARTGATE.*?ENDGATE/gms;

		// Extracting all occurrences of STARTGATE and ENDGATE blocks
		const gates = inputString.match(gateRegex) || [];

		// Removing the STARTGATE and ENDGATE blocks from the input string
		const trimmedString = inputString.replace(gateRegex, '');

		// Extracting individual lines from the trimmed string
		const lines = trimmedString
			.split('\n')
			.map((line) => line.trim())
			.filter((line) => line !== '');

		// Combining lines and gates
		const result = [...lines].join('\n');
		// const result = [...gates].join('\n');

		return result;
	}


	possibleViewers = generatePossibleViewers(shdl);
</script>

<div>
	{#each possibleViewers as possibleViewer, i}
		<button class="pr-5">{possibleViewer}</button>
	{/each}
</div>
<Canvas {width} {height} shdl={parseText(shdl)} />
