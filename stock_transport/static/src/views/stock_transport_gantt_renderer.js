/* @odoo-module */


import { GanttRenderer } from "@web_gantt/gantt_renderer";
import { useService } from "@web/core/utils/hooks"
import { useEffect, onWillStart } from "@odoo/owl";

export class StockTransportGanttRenderer extends GanttRenderer {
    setup() {
        super.setup();
        useEffect(() => {
            this.rootRef.el.classList.add("o_stock_transport_gantt");
        });
        this.userService = useService('user');
        // onWillStart(this.onWillStart);
    }
    getDriverImage(pill) {
        const { record } = pill;
        if (record.driver_image) {
            return record.driver_image;
        } else {
            return null;
        }
    }
    /**
     * @override
     */
    enrichPill(pill) {
        super.enrichPill(...arguments);

        pill.driver_image = this.getDriverImage(pill);
        return pill;
    }

    /**
     * @override
     */

    getDisplayName(pill) {
        var labelElements = super.getDisplayName(...arguments);
        const { record } = pill;
        if (record.weight) {
            labelElements = labelElements.concat(`( ${record.weight}`);   
        }
        if (record.volume) {
            labelElements = labelElements.concat(`, ${record.volume})`);
        }
        return labelElements;
    }
    
}
StockTransportGanttRenderer.pillTemplate = "stock_transport.StockTransportGanttRenderer.Pill";
StockTransportGanttRenderer.components = {
    ...GanttRenderer.components,
};
