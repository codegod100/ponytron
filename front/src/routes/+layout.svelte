<script>
  import Login from "$lib/Login.svelte";
  export let data;
  console.log("layout data", data);
  import { storedname } from "$lib/common";
</script>

<h1>Ponytron 🐴</h1>
<Login username={data.username} />
{#if $storedname}
  <slot />
{/if}
