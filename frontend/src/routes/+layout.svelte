<script lang="ts">
	import "./layout.css";
	import favicon from "$lib/assets/favicon.svg";

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div
	class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-4"
>
	<main>
		{@render children()}
	</main>
</div>
