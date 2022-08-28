import buildTree from '../helpers/tree';
import print from './print';
import evalCommand from './evalCommand';
import typeText from './typeText';
import { startProcess, stopProcess } from './process';
import { attachKeyboardListener } from '../helpers/keyboard';
import { dispatchEvent } from '../helpers/events';
import createHelp from '../helpers/help';
import loadStyle from '../helpers/loadStyle';
const initTerminal = ({ host, welcomeMessage, prompt = '$: ', historyLength = 50, enableHelp = true, commands }) => {
    const settings = {
        host,
        welcomeMessage,
        prompt,
        historyLength,
        enableHelp,
        commands
    };
    loadStyle();
    const { commandContainer, input, inputContainer } = buildTree(host, prompt);
    const terminal = {
        history: [],
        lastHistoryIndex: 0,
        isProcessRunning: false,
        settings,
        commandContainer,
        inputContainer,
        input,
        print: (content, isCommand = false) => print(content, isCommand, commandContainer, input, prompt),
        run: (cmd) => evalCommand(cmd, terminal),
        start: () => startProcess(terminal),
        stop: () => stopProcess(terminal),
        type: (text, speed = 60, callback) => typeText(text, speed, terminal, callback)
    };
    if (enableHelp) {
        terminal.settings.commands.help = createHelp(terminal);
    }
    attachKeyboardListener(host, terminal);
    dispatchEvent("onInit" /* ON_INIT */, host);
    welcomeMessage && (terminal.print(welcomeMessage));
    return terminal;
};
export default initTerminal;
