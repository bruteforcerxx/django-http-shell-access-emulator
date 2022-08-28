export declare const enum TerminalEvent {
    ON_COMMAND = "onCommand",
    ON_COMMAND_NOT_FOUND = "onCommand404",
    ON_PROCESS_START = "onProcessStart",
    ON_PROCESS_END = "onProcessStop",
    ON_PROCESS_INTERRUPT = "onProcessInterrupt",
    ON_INIT = "onInit"
}
export declare const dispatchEvent: (event: TerminalEvent, host: HTMLElement, info?: string) => void;
