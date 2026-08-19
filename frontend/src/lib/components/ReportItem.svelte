<script lang="ts">
    import type { Report } from "$lib/types/report";

    let {
        report,
        handleStatus,
    }: {
        report: Report;
        handleStatus: (id: number) => void;
    } = $props();
</script>

<div class="flex items-center gap-1">
    <p class="text-sm text-white">
        {report.id}. {report.email}:{report.type}. Статус: {report.status}
    </p>
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
