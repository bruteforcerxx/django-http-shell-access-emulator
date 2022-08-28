import { TerminalInstance } from './terminal';
export declare type TerminalCommand = {
    name: string;
    description: string;
    argDescriptions?: string[];
    func: (terminal: TerminalInstance, ...args: string[]) => void;
};
