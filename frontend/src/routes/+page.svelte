<script lang="ts">
    import type { Report } from "$lib/types/report";
    import ReportItem from "$lib/components/ReportItem.svelte";
    import ReportForm from "$lib/components/ReportForm.svelte";

    let email = $state("");
    let reportType = $state("Sales");
    let count = 1;
    let isSubmitted = $state(false);
    let isGenerated = $state(false);

    let reports = $state<Report[]>([]);

    let totalReport = $derived(reports.length);
    let completedReport = $derived(
        reports.filter((x) => x.status == "completed").length,
    );
    let processingReport = $derived(
        reports.filter((x) => x.status == "processing").length,
    );
    function handleSubmit() {
        if (!email.trim()) return;
        isSubmitted = true;
        console.log("prviet");
        reports.push({
            id: count++,
            type: reportType,
            email: email,
            status: "queued",
        });
        setTimeout(() => (isSubmitted = false), 2000);
    }

    function handleStatus(reportId: number) {
        const report = reports.find((x) => x.id == reportId);
        if (!report) return;
        switch (report.status) {
            case "queued":
                report.status = "processing";
                break;
            case "processing":
                report.status = "completed";
                break;
        }
    }

    async function generateReport(){
        await new Promise((resolve) => {
        setTimeout(resolve, 3000);
        });
        isGenerated = true
    }
</script>

<section>
    <h1 class="font-bold text-white text-4xl text-center pt-5">
        Добро пожаловать
    </h1>
    <div
        class="w-full max-w-md bg-slate-800/50 backdrop-blur-xl rounded-2xl p-8 shadow-2xl border border-slate-700 mt-5"
    >
        <ReportForm bind:email bind:reportType {handleSubmit} {isSubmitted} />

        <div class="text-center pt-10">
            <label class=" text-white font-bold text-sm">
                Недавние отчёты:
            </label>
            <div class="flex items-center gap-3">
                <p class="text-sm text-white">Всего: {totalReport}</p>
                <p class="text-sm text-white">
                    В процессе: {processingReport == undefined
                        ? 0
                        : processingReport}
                </p>
                <p class="text-sm text-white">
                    Завершенные: {completedReport == undefined
                        ? 0
                        : completedReport}
                </p>
            </div>

            {#each reports as report}
                <ReportItem {report} {handleStatus} />
            {/each}
        </div>
    </div>
</section>
