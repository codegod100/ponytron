<script>
    import Login from "$lib/Login.svelte"
    export let data
    console.log("layout data", data)
</script>
<h1>Ponytron 🐴</h1>
<Login username={data.username}/>
<slot/>