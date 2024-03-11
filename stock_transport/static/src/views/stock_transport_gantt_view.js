/* @odoo-module */

import { registry } from "@web/core/registry";
import { ganttView } from "@web_gantt/gantt_view";
import { StockTransportGanttRenderer } from "./stock_transport_gantt_renderer";

const viewRegistry = registry.category("views");

export const StockTransportGanttView = {
    ...ganttView,
    Renderer: StockTransportGanttRenderer,
};

viewRegistry.add("stock_transport_gantt", StockTransportGanttView);
