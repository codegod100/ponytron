<script>
    export let logged_in = false
</script>
{#if !logged_in}
Username or Email
<input type="text">
Password
<input type="text">
{/if}