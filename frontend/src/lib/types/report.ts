export interface Report {
    id: number;
    type: string;
    email: string;
    status: "queued" | "processing" | "completed";
}

export interface ReportRespone {
    type: string;
    email: string;
    status: "queued" | "processing" | "completed";
}

export interface API {
    message: string
    status: string
}
