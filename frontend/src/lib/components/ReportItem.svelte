<script lang="ts">
    import type { Report } from "$lib/types/report";
    import type { API } from "$lib/types/report";
    import { onMount } from "svelte";
    let {
        report,
        handleStatus,
    }: {
        report: Report;
        handleStatus: (id: number) => void;
    } = $props();

    let data = $state<API | null>(null);
    let loading = $state(true);
    let error = $state<string | null>(null);

    async function getHello(): Promise<API> {
        try {
            const respone = await fetch(
                "http://127.0.0.1:8000/health/?text=privet",
                {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        Accept: "application/json",
                    },
                },
            );

            if (!respone.ok) {
                throw new Error(`HTTP Error: ${respone.status}`);
            }

            const data: API = await respone.json();
            return data;
        } catch (error) {
            throw new Error(`Error: ${error}`);
        }
    }

    onMount(async () => {
        try {
            data = await getHello();
        } catch (err) {
            error = err instanceof Error ? err.message : "Unknown error";
        } finally {
            loading = false;
        }
    });
</script>

<div class="flex items-center gap-1">
    <p class="text-sm text-white">
        {report.id}. {report.email}:{report.type}. Статус: {report.status}
    </p>
    {#if loading}
        <p>Loading...</p>
    {:else if error}
        <p>Error: {error}</p>
    {:else if data}
        <p>{data.message}</p>
    {/if}
    <button
        disabled={report.status == "completed"}
        onclick={() => handleStatus(report.id)}
        class="
                        text-orange-600 font-semibold text-sm
                        py-2 px-6 rounded-full
                        border-2 border-orange-500
                        bg-transparent
                        transition-all duration-300
                        hover:bg-orange-500 hover:text-white
                        hover:shadow-lg hover:border-orange-600
                        disabled:opacity-50 disabled:cursor-not-allowed
                        disabled:hover:bg-transparent disabled:hover:text-orange-600
                        focus:outline-none focus:ring-2 focus:ring-orange-400 focus:ring-offset-2
                        min-w-[100px]
                        "
    >
        {#if report.status == "queued"}
            Начать
        {:else if report.status == "completed"}
            Завершено ✓
        {:else}
            Действие
        {/if}
    </button>
</div>
