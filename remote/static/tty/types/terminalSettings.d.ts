import { TerminalCommand } from './terminalCommand';
export declare type TerminalSettings = {
    host: HTMLElement;
    commands: Record<string, TerminalCommand>;
    welcomeMessage?: string;
    prompt?: string;
    historyLength?: number;
    enableHelp?: boolean;
};
