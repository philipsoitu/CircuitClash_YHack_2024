<script>
	import Visualizer from '../components/Visualizer.svelte';
	let text = '';
	$: shdl = text;
</script>

<div class="mx-5 my-5">
	<Visualizer width={500} height={500} {shdl} />
</div>
