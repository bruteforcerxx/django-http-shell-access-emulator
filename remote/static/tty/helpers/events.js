export const dispatchEvent = (event, host, info) => {
    const customEvent = new CustomEvent(event, { detail: info });
    host.dispatchEvent(customEvent);
};
