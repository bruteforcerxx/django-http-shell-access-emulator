import { TerminalInstance, TerminalSettings } from '../types';
declare const initTerminal: ({ host, welcomeMessage, prompt, historyLength, enableHelp, commands }: TerminalSettings) => TerminalInstance;
export default initTerminal;
