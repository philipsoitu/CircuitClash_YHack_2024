<script>
	import Visualizer from '../../components/Visualizer/Visualizer.svelte';
	let text = `INPUT A
INPUT B
OUTPUT C
AND A B C`;
</script>

<div style="width: 100%; display: table;">
	<div style="display: table-row">
		<div style="width: 600px; display: table-cell;">
			<textarea 
                bind:value={text}
				on:input={() => {
					text = text;
				}}
			/>
		</div>
		<div style="display: table-cell;"><Visualizer width={500} height={350} shdl={text} /></div>
	</div>
</div>

<style>
	textarea {
		width: 100%;
		height: 200px;
	}
</style>
